# pulse-schemas

A Python package for managing user profile schemas using Pydantic.

## Features

- Schema registry to store and retrieve Pydantic models
- Easily extensible for custom schemas

## Installation

```
pip install pulse-schemas
```

## Usage

This project includes a **schema manager** (`SchemaRegistry`) that makes it easy to register, retrieve, and validate Pydantic schemas. A default schema for creating a user profile is already included.

### Import the registry

```
from pulse_schemas.schema import SchemaRegistry
```

### Initialize the registry

```
registry = SchemaRegistry()
```

When initialized, the registry automatically registers the built-in schema `create_user_profile`.

### List available schemas

```
print(registry.list_schemas())
# ['create_user_profile']
```

### Retrieve a schema

```
ProfileSchema = registry.get_schema("create_user_profile")
```

### Validate data against a schema

```
data = {
    "demographics": {"age": 28, "biological_sex": "female"},
    "dietary_preferences": ["vegetarian"],
    "allergens": ["peanuts", "milk"],
    "health_conditions": ["hypertension"],
    "goals": ["improve cardio"]
}

profile = ProfileSchema.model_validate(data)
print(profile)
```

If the data is invalid, Pydantic will raise a `ValidationError`.

### Register custom schemas

You can register new schemas at runtime:

```python
from pydantic import BaseModel

class CustomSchema(BaseModel):
    name: str
    active: bool

registry.register_schema("custom_schema", CustomSchema)
print(registry.list_schemas())
# ['create_user_profile', 'custom_schema']
```

Now you can retrieve and validate against `custom_schema` in the same way.

