from __future__ import annotations
import os
import re
import sys
import time
import pathlib
import typing as t
from dataclasses import dataclass

import requests

GITHUB_API = os.environ.get("GITHUB_API", "https://api.github.com")
DEFAULT_TIMEOUT = 30

class GHCPError(RuntimeError):
    pass

@dataclass
class ParsedURL:
    owner: str
    repo: str
    ref: str | None
    path: str | None
    kind: str  # "tree" or "blob" or "root"

_GH_URL_RE = re.compile(r"^https?://github.com/([^/]+)/([^/]+)(?:/(tree|blob)/([^/]+)(?:/(.*))?)?/?$")


def parse_github_url(url: str) -> ParsedURL:
    m = _GH_URL_RE.match(url)
    if not m:
        raise GHCPError(
            "URL must look like https://github.com/<owner>/<repo>[/tree|blob/<ref>/<path>]"
        )
    owner, repo, kind, ref, path = m.groups()
    if kind is None:
        return ParsedURL(owner, repo, None, None, "root")
    return ParsedURL(owner, repo, ref, path or "", kind)


def _headers(token: str | None) -> dict[str, str]:
    h = {"Accept": "application/vnd.github.v3+json", "User-Agent": "ghcp/0.1"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def get_default_branch(owner: str, repo: str, token: str | None) -> str:
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    r = requests.get(url, headers=_headers(token), timeout=DEFAULT_TIMEOUT)
    if r.status_code == 404:
        raise GHCPError("Repository not found or you lack access.")
    r.raise_for_status()
    return r.json().get("default_branch", "main")


def iter_directory(owner: str, repo: str, path: str, ref: str, token: str | None) -> t.Iterator[dict]:
    # Uses the Contents API recursively
    api = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
    params = {"ref": ref}
    r = requests.get(api, headers=_headers(token), params=params, timeout=DEFAULT_TIMEOUT)
    if r.status_code == 404:
        raise GHCPError(f"Path not found: {path} @ {ref}")
    r.raise_for_status()
    items = r.json()
    if not isinstance(items, list):
        # It's a file, not a directory
        yield items
        return

    stack = [(path, items)]
    while stack:
        base, children = stack.pop()
        for it in children:
            tpe = it.get("type")
            if tpe == "file":
                yield it
            elif tpe == "dir":
                sub_api = it["url"]  # contents API URL
                r2 = requests.get(sub_api, headers=_headers(token), timeout=DEFAULT_TIMEOUT)
                r2.raise_for_status()
                stack.append((it["path"], r2.json()))
            elif tpe in ("symlink", "submodule"):
                # Skip special entries but warn
                yield {"type": tpe, **it}
            else:
                yield {"type": tpe or "unknown", **it}


def download_url(url: str, outdir: str | None = None, ref: str | None = None,
                 token: str | None = None, preserve: bool = False, quiet: bool = False) -> pathlib.Path:
    """Download a GitHub folder or file URL into *outdir*.

    - If *preserve* is True, keep full repo path under outdir.
    - If *ref* is None, resolves repo default branch.
    - *token* may be provided or taken from env GITHUB_TOKEN.
    Returns the local destination path (folder or file).
    """
    token = token or os.environ.get("GITHUB_TOKEN")
    p = parse_github_url(url)

    # Determine reference
    ref = ref or p.ref
    if not ref:
        ref = get_default_branch(p.owner, p.repo, token)

    # Decide what to download
    base_out = pathlib.Path(outdir or ".").resolve()

    if p.kind == "blob":
        # Single file
        file_api = f"{GITHUB_API}/repos/{p.owner}/{p.repo}/contents/{p.path}"
        r = requests.get(file_api, headers=_headers(token), params={"ref": ref}, timeout=DEFAULT_TIMEOUT)
        if r.status_code == 404:
            raise GHCPError(f"File not found: {p.path} @ {ref}")
        r.raise_for_status()
        meta = r.json()
        if meta.get("type") != "file":
            raise GHCPError("URL points to a directory, not a file.")
        # destination
        dest = base_out
        if dest.is_dir():
            name = pathlib.Path(p.path).name if not preserve else pathlib.Path(p.path)
            dest = dest / name
        _stream_download(meta["download_url"], dest, token)
        if not quiet:
            print(f"Downloaded {dest}")
        return dest

    # tree or root => directory mode
    folder_path = p.path or ""
    if not folder_path:
        # downloading repo root; keep repo name as top folder
        top = p.repo if preserve else p.repo
    else:
        top = folder_path if preserve else pathlib.Path(folder_path).name

    target_root = base_out / top
    target_root.mkdir(parents=True, exist_ok=True)

    for item in iter_directory(p.owner, p.repo, folder_path or "", ref, token):
        tpe = item.get("type")
        if tpe == "file":
            rel = pathlib.Path(item["path"]) if preserve else pathlib.Path(item["path"]).relative_to(folder_path) if folder_path else pathlib.Path(item["name"])
            dest = target_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            _stream_download(item["download_url"], dest, token)
            if not quiet:
                print(f"Downloaded {dest}")
        elif tpe in ("symlink", "submodule"):
            if not quiet:
                print(f"Skipping {tpe}: {item.get('path')}")
        else:
            # unknown entry types are ignored but noted
            if not quiet:
                print(f"Skipping unknown entry: {item.get('path')} ({tpe})")

    return target_root


def _stream_download(url: str, dest: pathlib.Path, token: str | None):
    headers = {"User-Agent": "ghcp/0.1"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with requests.get(url, headers=headers, stream=True, timeout=DEFAULT_TIMEOUT) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 256):
                if chunk:
                    f.write(chunk)