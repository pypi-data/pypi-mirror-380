# lacardlabs (placeholder)

This is a placeholder release that reserves the `lacardlabs` project name on PyPI while the real
source code remains private.

- No runtime functionality is provided.
- Version is pinned at `0.0.0a0` until the full project is published.
- The Trove classifier `Development Status :: 1 - Planning` signals that this is an intentional placeholder.

To publish the placeholder:

```bash
python -m build
python -m twine upload dist/*
```

After publishing, you may also yank the release so it is skipped by installers by default:

```bash
twine yank lacardlabs 0.0.0a0
```
