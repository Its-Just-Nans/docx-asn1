# CHANGELOG

## Create a new version

```sh
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m pip install --upgrade twine
rm -rf dist/ build/
python3 -m build
# create egg-info folder
python3 -m twine upload dist/* --verbose
# use __token__ auth
# enter token
```

## 2025-10-20

- edit README
- proper bump of version

## 2025-10-18

- add `python-docx` dependency

## 2024-05-30

- add test (`python -m pytest`)
- fix asn1 output - docx package does not handle smarttags

## 2024-04-26

- add custom start and end

## 2024-03-13

- Create package
