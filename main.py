import numpy as np
from PIL import Image
from easyocr import Reader
from wordsegment import load, segment


def main():
    parchment = Image.open('parchment.png')

    # Extract visible text
    blue_channel = parchment.getchannel('B')
    extracted_image = blue_channel.point(lambda v: 255 if v < 230 else 0)

    # Extract text from image
    reader = Reader(lang_list=['en'])
    orc_result = reader.readtext(
        np.array(extracted_image),
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
