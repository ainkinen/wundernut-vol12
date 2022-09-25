from easyocr import Reader  # type: ignore
from wordsegment import load, segment  # type: ignore

from src.img_utils import extract_img_data


def main():
    img_data = extract_img_data('parchment.png')

    # Extract text from image
    reader = Reader(lang_list=['en'])
    orc_result = reader.readtext(
        img_data,
        allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        paragraph=True,
        detail=0,  # Simplified output. Only the extracted paragraphs.
    )[0]
    extracted_text = orc_result.replace(' ', '')  # Remove whitespace to get lines as a continuous string
    print(f'{extracted_text=}')

    # Decrypt text
    rot5 = ''.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'FGHIJKLMNOPQRSTUVWXYZABCDE')  # Ceasar cipher with a shift of 5
    decrypted_text = extracted_text.translate(rot5)
    print(f'{decrypted_text=}')

    # Segment text for readability
    load()
    segments = segment(decrypted_text)
    segmented_text = ' '.join(segments)
    print(f'{segmented_text=}')


if __name__ == "__main__":
    main()
