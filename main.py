from wordsegment import load, segment  # type: ignore

from src.crypto_utils import rot5_decrypt
from src.img_utils import extract_img_data
from src.ocr import extract_paragraph


def main():
    img_data = extract_img_data('parchment.png')

    extracted_text = extract_paragraph(img_data)
    print(f'{extracted_text=}')

    decrypted_text = rot5_decrypt(extracted_text)
    print(f'{decrypted_text=}')

    # Segment text for readability
    load()
    segments = segment(decrypted_text)
    segmented_text = ' '.join(segments)
    print(f'{segmented_text=}')


if __name__ == "__main__":
    main()
