from functools import cache

import wordsegment as ws  # type: ignore


@cache
def _load_word_data():
    ws.load()


def segment(input_str: str) -> str:
    _load_word_data()
    segments = ws.segment(input_str)
    return ' '.join(segments)
