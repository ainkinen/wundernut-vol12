from wordsegment import load, segment as wordsegment  # type: ignore

load()


def segment(input_str: str) -> str:
    segments = wordsegment(input_str)
    return ' '.join(segments)
