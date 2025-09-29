
# CVNN_Jamie: Complex-Valued Neural Network Framework

CVNN_Jamie is a Python library for building and training complex-valued neural networks. It provides modular layers, a flexible Sequential model, a wide range of complex activation functions, and custom initialisation methods. Designed for research and experimentation with complex-valued data and models.

## Features
- Complex-valued layers (Dense, Activation, etc.)
- Modular and extensible design
- Custom activation functions and derivatives
- Multiple initialisation methods (including custom/phase-constrained)
- Easy integration with NumPy
- Simple Sequential API for stacking layers and activations
- Full backpropagation and training support

## Installation

Install from PyPI:
```sh
pip install CVNN_Jamie
```
Or from source:
```sh
pip install -r requirements.txt
```

---

## Model API: Sequential


You can easily build single-layer or multilayer networks using the `Sequential` model (import from `cvnn`):

### Single-Layer Network
```python
from cvnn import Sequential
from cvnn.layers import ComplexDense
from cvnn.activations import complex_relu
import numpy as np

model = Sequential([
	ComplexDense(input_dim=4, output_dim=2),
	complex_relu
])
x = np.random.randn(1, 4) + 1j * np.random.randn(1, 4)
out = model.forward(x)
print("Single-layer output:", out)
```

### Multilayer Network
```python
from cvnn import Sequential
from cvnn.layers import ComplexDense
from cvnn.activations import complex_relu, complex_tanh
import numpy as np

model = Sequential([
	ComplexDense(input_dim=4, output_dim=8),
	complex_relu,
	ComplexDense(input_dim=8, output_dim=2),
	complex_tanh
])
x = np.random.randn(1, 4) + 1j * np.random.randn(1, 4)
out = model.forward(x)
print("Multilayer output:", out)
```

### Training (Demo: 1-layer, MSE loss, SGD)
```python
from cvnn import Sequential
from cvnn.layers import ComplexDense
import numpy as np

# Dummy data: learn identity mapping
x = np.random.randn(10, 2) + 1j * np.random.randn(10, 2)
y = x.copy()
model = Sequential([
	ComplexDense(input_dim=2, output_dim=2)
])
model.fit(x, y, epochs=50, lr=0.01)
```
# Complex-Valued Neural Network (CVNN) Framework

This library provides a framework for building complex-valued neural networks in Python. It includes core modules for layers, activations, and operations that support complex numbers.

## Features
- Complex-valued layers (Dense, Activation, etc.)
- Modular and extensible design
- Easy integration with NumPy

## Getting Started

Install requirements:
```
pip install -r requirements.txt
```


## Example Usage

### ComplexDense Layer with Custom Initialisation
```python
from cvnn.layers import ComplexDense
from cvnn.activations import complex_glorot_uniform, jamie
import numpy as np

# Use Glorot uniform for weights, jamie for bias
layer = ComplexDense(input_dim=4, output_dim=2, weight_init=complex_glorot_uniform, bias_init=jamie)
x = np.random.randn(1, 4) + 1j * np.random.randn(1, 4)
out = layer.forward(x)
print(out)
```

### Using Activation Functions
```python
from cvnn.activations import complex_relu, complex_sigmoid, complex_tanh, modrelu

z = np.array([1+2j, -1-2j, 0+0j, -3+4j])
print("ReLU:", complex_relu(z))
print("Sigmoid (separable):", complex_sigmoid(z))
print("Sigmoid (fully complex):", complex_sigmoid(z, fully_complex=True))
print("Tanh (separable):", complex_tanh(z))
print("Tanh (fully complex):", complex_tanh(z, fully_complex=True))
print("modReLU:", modrelu(z, bias=0.5))
```

### Using Initialisation Methods Directly
```python
from cvnn.activations import complex_zeros, complex_ones, complex_normal, complex_glorot_uniform, complex_he_normal, jamie

w = complex_zeros((3, 2))
b = jamie((1, 2))
print("Zeros init:", w)
print("Jamie init:", b)
```

## License
MIT
