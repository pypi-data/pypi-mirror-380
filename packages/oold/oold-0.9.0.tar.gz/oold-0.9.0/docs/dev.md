# Setup
1. create a virtual environment
```bash
python -m venv .venv
```

1. install requirements + extras
```bash
pip install -e .[dev,testing]
```


# Testing

1. Create new test (file name test_*.py) under /tests

1. Run pytest in the project root dir
```bash
tox -e test
```
