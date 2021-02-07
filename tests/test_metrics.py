import pytest

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


def test_wer():
    assert pywer.wer(references, hypotheses) == 25.0


def test_cer():
    assert pytest.approx(pywer.cer(references, hypotheses), 0.0001) == 14.1176
