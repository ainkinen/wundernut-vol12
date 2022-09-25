from wordsegment import load, segment  # type: ignore

from src.img_utils import extract_img_data
from src.ocr import extract_paragraph


def main():
    img_data = extract_img_data('parchment.png')

    extracted_text = extract_paragraph(img_data)
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
