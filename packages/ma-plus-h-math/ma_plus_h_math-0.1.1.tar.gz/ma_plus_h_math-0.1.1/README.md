# ma+h

A simple Python library for mathematical functions.

## Installation

```bash
pip install ma-plus-h-math
```

## Usage

```python
from ma+h import sine
import math

# Calculate sine of 0
result = sine(0)
print(result)  # 0.0

# Calculate sine of π/2
result = sine(math.pi/2)
print(result)  # 1.0

# Calculate sine of π
result = sine(math.pi)
print(result)  # 0.0
```

## Functions

### sine(x)

Calculate the sine of an input value.

**Parameters:**
- `x` (int or float): Input value in radians

**Returns:**
- `float`: The sine value of the input

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
