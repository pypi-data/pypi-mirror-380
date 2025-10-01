# ODM Helper Decorations

Python decorators for ETL functions with logging and error handling.

## Installation

```bash
pip install odm-hlp-decorations
```

## Usage

```python
from odm_hlp_decorations import task

@task()
def my_function():
    # Your code here
    pass
```

## Requirements

- Python 3.8+
- python-dotenv

## Configuration

Create a `.env` file with:
```
logs_path=./logs/
```

## License

MIT