# Pi Library

pilibr is a simple Python package for performing calculations with π (Pi).  
It provides a symbolic Pi class as well as functions for approximating Pi using different methods.

## Installation

You can install the package via pip/npm:

```bash
pip install pilibr
npm install pilibr
```

Or install locally for development:

Currently not supported. Please check back in version 0.0.2.

## Usage

### Using the Pi class

```python
from pilibr import Pi

# Create Pi objects
pi_default = Pi()       # 1 * π / 1
pi_half = Pi(1, 2)      # 1 * π / 2

# Symbolic representation
print(pi_default)       # 1 * π / 1

# Numerical approximation
print(pi_default.evall(10000))   # Leibniz method
print(pi_default.evaln(5000))    # Nilakantha method
```

### Using the helper function `pif`

```python
from pilibr import pif

# Approximate Pi using the Leibniz series
print(pif(method="leibniz", iterations=10000))

# Approximate Pi using the Nilakantha series
print(pif(method="nilakantha", iterations=5000))
```

## Features

* Symbolic Pi representation
* Approximation using:

  * Leibniz series
  * Nilakantha series
* Easy-to-use helper function `pif`

## License

This project is licensed under the Apache-2.0 License.