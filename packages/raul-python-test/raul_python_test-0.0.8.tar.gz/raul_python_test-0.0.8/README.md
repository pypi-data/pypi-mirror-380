# test-python

This is a dummy Python project to test deployment to PyPi and GitHub Actions.

## Notes

### Build

```bash
python -m build . -o dist
```

### Deploy

[Using TestPyPi](https://packaging.python.org/en/latest/guides/using-testpypi/#using-test-pypi)

[Deploy to PyPi](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi)

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=<insert_password>
twine upload --repository testpypi dist/*
```

### Run

```bash
raul-python-test
```
