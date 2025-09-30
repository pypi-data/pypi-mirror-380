# Ontologia

An ontology management system built on Registro and SQLModel.

## Overview

Ontologia provides a structured way to define and manage ontologies using SQLModel (SQLAlchemy + Pydantic). It leverages Registro for resource identification, validation, and lifecycle management.

## Features

- **Object Types**: Define object structures with properties and relationships
- **Property Types**: Rich data type system including basic and composite types
- **Link Types**: Manage relationships between object types with cardinality
- **Validation**: Ensures referential integrity and type safety
- **SQLModel Integration**: Automatic table creation and ORM operations

## Installation

```bash
pip install ontologia
```

## Usage

See `main.py` for example usage of creating object types, properties, and relationships.

## Development

```bash
# Install dependencies
uv sync

# Run tests (if tests directory exists)
uv run pytest tests/

# Run example
uv run python main.py
```

## License

MIT
