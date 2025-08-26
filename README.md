# Offline Tool Evals

Evaluate scripted tool-use traces with allowlists, argument validation, bounded execution and reproducible local cases.

## Run locally

Use a currently supported Python 3 interpreter. No third-party packages, credentials, downloads, or network access are required.

```sh
python -m unittest discover -s tests -v
python demo.py
```

Run from the repository directory. The demo reads `examples/input.json`; inputs are reproducible, authored examples.

## Scope and behavior

Scripts act as provider fakes: they specify tool requests and final answers without calling an AI service. Exact status and answer assertions measure the harness contract, not language-model intelligence or factual accuracy. Only supplied tools can run; this is not an operating-system sandbox for untrusted Python functions. The local step format is intentionally independent of any vendor SDK or Chat Completions schema.

## Layout

- `core.py`: primary algorithm or storage contract.
- `features.py`: pipeline or integration layer.
- `tests/`: independent behavioral assertions, failure cases, and regressions.
- `demo.py` and `examples/input.json`: repeatable end-to-end example.

## Example output

```json
{
  "pass_rate": 1.0,
  "passed": 3,
  "results": [
    {
      "actual": {
        "answer": "7",
        "status": "answered",
        "trace": [
          {
            "ok": true,
            "output": 7,
            "tool": "add"
          }
        ]
      },
      "id": "arithmetic",
      "passed": true
    },
    {
      "actual": {
        "answer": null,
        "status": "denied",
        "trace": []
      },
      "id": "forbidden",
      "passed": true
    },
    {
      "actual": {
        "answer": null,
        "status": "step_budget",
        "trace": []
      },
      "id": "exhaustion",
      "passed": true
    }
  ],
  "total": 3
}
```

## Compatibility and license

The implementation uses language features and standard-library APIs available in [Python 3.4](https://docs.python.org/3.4/library/index.html), released in [March 2014](https://www.python.org/downloads/release/python-340/). Use a supported runtime; an old interpreter is not required. Compatibility with a historical runtime is not certified by current-runtime tests.

MIT licensed. No third-party source code or datasets are bundled.
