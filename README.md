# pywer
![pytest](https://github.com/jumon/pywer/workflows/pytest/badge.svg)

Pywer is a simple Python package to calculate word error rate (WER). Pywer can also
calculate character error rate (CER).

## Install
You can install pywer via pip.
```
pip install pywer
```

## Usage
```python
import pywer

references = [
    "this is a simple python package",
    "it calculates word error rate",
    "it can also calculate cer",
]
hypotheses = [
    "this is the simple python package",
    "it calculates word error",
    "it can also calculate see er",
]

wer = pywer.wer(references, hypotheses)
cer = pywer.cer(references, hypotheses)
print(f"WER: {wer:.2f}, CER: {cer:.2f}")
```

## Development
Install pre-commit hooks.
```
pip install pre-commit
pre-commit install --install-hooks
```
