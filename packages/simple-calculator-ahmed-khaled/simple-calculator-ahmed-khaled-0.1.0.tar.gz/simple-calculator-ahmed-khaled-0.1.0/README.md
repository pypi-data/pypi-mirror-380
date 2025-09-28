'''# Simple Calculator - Ahmed Khaled

A simple Python library for basic arithmetic operations: addition, subtraction, multiplication, and division.

## Installation

To install the package, use the following command:

```bash
pip install simple-calculator-ahmed-khaled
```

## Usage

```python
from simple_calculator_ahmed_khaled.calculator import add, subtract, multiply, divide

# Addition
result_add = add(15, 7)
print(f"Addition: {result_add}")

# Subtraction
result_subtract = subtract(15, 7)
print(f"Subtraction: {result_subtract}")

# Multiplication
result_multiply = multiply(15, 7)
print(f"Multiplication: {result_multiply}")

# Division
result_divide = divide(15, 7)
print(f"Division: {result_divide}")

# Division by zero
try:
    divide(15, 0)
except ValueError as e:
    print(e)
```
'''
