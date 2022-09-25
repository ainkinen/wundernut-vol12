from functools import cache

import numpy as np
from easyocr import Reader  # type: ignore


@cache
def _reader(langs: list[str] | None = None):
    if langs is None:
        langs = ['en']
    return Reader(lang_list=langs)


def extract_paragraph(
        img_data: np.typing.ArrayLike,
        allowed_chars: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
) -> str:
    orc_result = _reader().readtext(
        img_data,
        allowlist=allowed_chars,
        paragraph=True,
        detail=0,  # Simplified output. Only the extracted paragraphs.
    )

    paragraph = orc_result[0]

    # Remove whitespace to get lines as a continuous string
    return paragraph.replace(' ', '')
