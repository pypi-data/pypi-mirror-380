# stackifier

A Python package for stack data structures and stack-based utilities.

## Installation

```bash
pip install stackifier
```

## Features

- **Stack Data Structure**: Full-featured stack implementation with push, pop, peek operations
- **String Reversal**: Reverse strings using a stack
- **Bracket Matching**: Check if brackets/parentheses are balanced
- **Text Formatting**: Create beautiful ASCII stack visualizations

## Usage

### Basic Hello Function

```python
from stackifier import hi
print(hi("Bryan Lai"))
```

### Stack Operations

```python
from stackifier import Stack

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
print(f"Top element: {stack.peek()}")
print(f"Size: {stack.size()}")
print(f"Popped: {stack.pop()}")
```

### String Reversal

```python
from stackifier import reverse_string

text = "Hello, World!"
reversed_text = reverse_string(text)
print(reversed_text)
```

### Bracket Matching

```python
from stackifier import is_balanced

print(is_balanced("()[]{}"))
print(is_balanced("({[]})"))
print(is_balanced("([)]"))
```

### ASCII Stack Visualization

```python
from stackifier import create_ascii_stack

items = ["Python", "Java", "C++", "JavaScript"]
print(create_ascii_stack(items))
```

### Text Formatting

```python
from stackifier import stackify_text

print(stackify_text("Welcome to Stackifier!", width=40, char="="))
```

## Build & Publish

1. Install build tools:
```bash
python -m pip install build twine
```

2. Build the package:
```bash
python -m build
```

3. Upload to PyPI:
```bash
python -m twine upload dist/*
```

## Test Locally

Before publishing, you can test locally:
```bash
pip install -e .
```
