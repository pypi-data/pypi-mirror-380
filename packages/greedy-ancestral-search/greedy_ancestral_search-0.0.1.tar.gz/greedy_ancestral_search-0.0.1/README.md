# Greedy Ancestral Search

## Getting started

Using `uv` for dependency management.
Read [here](https://docs.astral.sh/uv/) for more information.

If you don't have it download it
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

To sync dependencies run
```
uv sync
```

## Testing

```
EXPORT PYTHONPATH=. && uv run pytest
```
## Benchmarks

```
uv run benchmarks/<script>.py
```

For the SERGIO benchmark, ensure you have SERGIO installed in the correct path.
Should be in `benchmarks/SERGIO`.
