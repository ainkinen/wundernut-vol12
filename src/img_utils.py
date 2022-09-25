import numpy as np
from PIL import Image  # type: ignore


def extract_img_data(filename: str) -> np.ndarray:
    image = Image.open(filename)

    # Extract visible text
    blue_channel = image.getchannel('B')
    extracted_image = blue_channel.point(lambda v: 255 if v < 230 else 0)

    return np.array(extracted_image)
