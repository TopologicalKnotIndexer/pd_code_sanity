# pd-code-sanity

Perform fast structural validation of planar-diagram codes.

## Installation

```bash
pip install pd-code-sanity
```

## Usage example

```python
from pd_code_sanity import sanity

print(sanity([[1, 2, 3, 4]]))       # False: labels occur once
print(sanity([[1, 1, 2, 2]]))       # True
print(sanity([[True, 1, True, 1]])) # False: bool is not a label
```

## Algorithm

Validation checks that the outer value and every crossing are lists, every crossing has exactly four entries, labels are consistently integers or strings, booleans are rejected, and every label occurs exactly twice. Counting uses `collections.Counter`, so runtime is linear in the number of crossing slots. This is structural validation; planarity is handled by the strong-sanity package.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
