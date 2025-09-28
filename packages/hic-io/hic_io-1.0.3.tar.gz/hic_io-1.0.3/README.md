## Installation

```
pip install hic-io
```

Requires numpy and pybind11.

## Usage

### Read signal

```python
reader = hic_io.Reader(path)
values = reader.read_signal(...)
```
