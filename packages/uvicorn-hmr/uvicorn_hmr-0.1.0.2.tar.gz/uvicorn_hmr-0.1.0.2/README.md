# uvicorn-hmr

[![PyPI - Version](https://img.shields.io/pypi/v/uvicorn-hmr)](https://pypi.org/project/uvicorn-hmr/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/uvicorn-hmr)](https://pepy.tech/projects/uvicorn-hmr)

This package provides hot module reloading (HMR) for [`uvicorn`](https://github.com/encode/uvicorn).

It uses [`watchfiles`](https://github.com/samuelcolvin/watchfiles) to detect FS modifications,
re-executes the corresponding modules with [`hmr`](https://github.com/promplate/pyth-on-line/tree/main/packages/hmr) and restart the server (in the same process).

**HOT** means the main process never restarts, and reloads are fine-grained (only the changed modules and their dependent modules are reloaded).
Since the python module reloading is on-demand and the server is not restarted on every save, it is much faster than the built-in `--reload` option provided by `uvicorn`.

## Why?

1. When you use `uvicorn --reload`, it restarts the whole process on every file change, but restarting the whole process is unnecessary:
   - There is no need to restart the Python interpreter, neither all the 3rd-party packages you imported.
   - Your changes usually affect only one single file, the rest of your application remains unchanged.
2. `hmr` tracks dependencies at runtime, remembers the relationships between your modules and only reruns necessary modules.
3. So you can save a lot of time by not restarting the whole process on every file change. You can see a significant speedup for debugging large applications.
4. Although magic is involved, we thought and tested them very carefully, so everything works just as-wished.
   - Your lazy loading through module-level `__getattr__` still works
   - Your runtime imports through `importlib.import_module` or even `__import__` still work
   - Even valid circular imports between `__init__.py` and sibling modules still work
   - Fine-grained dependency tracking in the above cases still work
   - Decorators still work, even meta programming hacks like `getsource` calls work too
   - Standard dunder metadata like `__name__`, `__doc__`, `__file__`, `__package__` are correctly set
   - ASGI lifecycles are preserved

Normally, you can replace `uvicorn --reload` with `uvicorn-hmr` and everything will work as expected, with a much faster refresh experience.

## Installation

```sh
pip install uvicorn-hmr
```

<details>

<summary> Or with extra dependencies: </summary>

```sh
pip install uvicorn-hmr[all]
```

This will install `fastapi-reloader` too, which enables you to use `--refresh` flag to refresh the browser pages when the server restarts.

> When you enable the `--refresh` flag, it means you want to use the `fastapi-reloader` package to enable automatic HTML page refreshing.
> This behavior differs from Uvicorn's built-in `--reload` functionality. (See the configuration section for more details.)
>
> Server reloading is a core feature of `uvicorn-hmr` and is always active, regardless of whether the `--reload` flag is set.
> The `--reload` flag specifically controls auto-reloading of HTML pages, a feature not available in Uvicorn.
>
> If you don't need HTML page auto-reloading, simply omit the `--reload` flag.
> If you do want this feature, ensure that `fastapi-reloader` is installed by running: `pip install fastapi-reloader` or `pip install uvicorn-hmr[all]`.

</details>

## Usage

Replace

```sh
uvicorn main:app --reload
```

with

```sh
uvicorn-hmr main:app
```

Everything will work as-expected, but with **hot** module reloading.

## CLI Arguments

I haven't copied all the configurable options from `uvicorn`. But contributions are welcome!

For now, `host`, `port`, `log-level`, `env-file` are supported and have exactly the same semantics and types as in `uvicorn`.

The behavior of `reload_include` and `reload_exclude` is different from uvicorn in several ways:

1. Uvicorn allows specifying patterns (such as `*.py`), but in uvicorn-hmr only file or directory paths are allowed; patterns will be treated as literal paths.
2. Uvicorn supports watching non-Python files (such as templates), but uvicorn-hmr currently only supports hot-reloading Python source files.
3. Uvicorn always includes/excludes all Python files by default (even if you specify `reload-include` or `reload-exclude`, all Python files are still watched/excluded accordingly), but uvicorn-hmr only includes/excludes the paths you specify. If you do not provide `reload_include`, the current directory is included by default; if you do provide it, only the specified paths are included. The same applies to `reload_exclude`.

The following options are supported but do not have any alternative in `uvicorn`:

- `--refresh`: Enables auto-refreshing of HTML pages in the browser whenever the server restarts. Useful for demo purposes and visual debugging. This is **totally different** from `uvicorn`'s built-in `--reload` option, which is always enabled and can't be disabled in `uvicorn-hmr` because hot-reloading is the core feature of this package.
- `--clear`: Wipes the terminal before each reload. Just like `vite` does by default.

The two features above are opinionated and are disabled by default. They are just my personal practices. If you find them useful or want to suggest some other features, feel free to open an issue.
