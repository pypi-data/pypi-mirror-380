# binScheme Parser

A parser for the binScheme language.

This library provides a parser for `.binscheme` files, which define binary data layouts. It parses the schema definition into a collection of Python data structures.

## Installation

```bash
pip install binscheme-parser
```

## Usage

To parse a `.binscheme` file, use the `load` function from the `binscheme_parser` module:

```python
from binscheme_parser import load

schema_collection = load('path/to/your/schema.binscheme')

# You can now access the parsed schemes, enums, and instances
print(schema_collection.schemes)
print(schema_collection.enums)
```
