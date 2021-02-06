from typing import List

import editdistance


def token_error_rate(refs: List[List[str]], hyps: List[List[str]]) -> float:
    """Calculate an error rate based on edit-distance.

    Args:
        refs (List[List[str]]): Reference sentences splitted into tokens.
        hyps (List[List[str]]): Automatic speech recognition (ASR) hypotheses splitted
            into tokens.

    Returns:
        float: Token error rate (multiplied by 100)
    """
    dist = 0
    ref_len = 0
    for ref, hyp in zip(refs, hyps):
        dist += editdistance.eval(ref, hyp)
        ref_len += len(ref)

    if ref_len:
        return dist * 100 / ref_len
    else:
        return 0


def wer(refs: List[str], hyps: List[str]) -> float:
    """Calculate word error rate (WER).

    Args:
        refs (List[str]): Reference sentences.
        hyps (List[str]): Automatic speech recognition (ASR) hypotheses.

    Returns:
        float: Word error rate (multiplied by 100)
    """
    ref_words = [ref.split() for ref in refs]
    hyp_words = [hyp.split() for hyp in hyps]
    return token_error_rate(ref_words, hyp_words)


def cer(refs: List[str], hyps: List[str]) -> float:
    """Calculate character error rate (CER).

    Args:
        refs (List[str]): Reference sentences.
        hyps (List[str]): Automatic speech recognition (ASR) hypotheses.

    Returns:
        float: Character error rate (multiplied by 100)
    """
    ref_words = [list(ref) for ref in refs]
    hyp_words = [list(hyp) for hyp in hyps]
    return token_error_rate(ref_words, hyp_words)
