# POSITION-ENCODING
A library that encodes sequence positions in torch.


# INSTALL

The package is installable using `pip`:

```
pip install position-encoding
```

## USAGE

Relative position encoding:

```python
from position_encoding import get_relative_position_encoding_matrix

# max length of sequence: 16
# encoding depth of each element: 32
m = get_relative_position_encoding_matrix(16, 32)
```

Absolute position encoding:

```python
from position_encoding import get_absolute_position_encoding

# max length of sequence: 16
# encoding depth of each element: 32
e = get_absolute_position_encoding(16, 32)
```
