# ghcp

Copy a folder or file from a GitHub repository using the GitHub API. No `git clone`, no `.git/` left behind.

## Install

```bash
pipx install ghcp  # once published
# or for local dev:  
pipx install -e .
```

## Usage

```bash
ghcp https://github.com/<owner>/<repo>/tree/<ref>/<path> -o ./out --preserve

ghcp https://github.com/<owner>/<repo>/blob/<ref>/<path> -o ./myfile
```

### Options

* `-o, --out`   Output directory (default: current dir)
* `--ref`       Branch, tag or commit SHA (default: repo default branch)
* `--token`     GitHub token (or set `GITHUB_TOKEN`)
* `--preserve`  Keep full repo path under the output directory
* `-q, --quiet` Reduce output

## Private repos / higher rate limits

Provide a token via `--token` or `GITHUB_TOKEN` environment variable.

## Limitations

* Git submodules and symlinks are skipped (not resolved).
* Very large repos may hit rate limits without a token.
