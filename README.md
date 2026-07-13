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

Validation checks that the outer value and every crossing are lists, every crossing has exactly four entries, labels are consistently integers or strings, booleans are rejected, and every label occurs exactly twice. Counting uses `collections.Counter`, so runtime is linear in the number of crossing slots. The empty code is accepted as the crossing-free unknot representation. This is structural validation only; it does not prove that arbitrary incidence data has a planar realization.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required.

## Development

Python 3.10 or newer is required. Run the regression tests with:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.
