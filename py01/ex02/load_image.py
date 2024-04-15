from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str):
    try:
        assert path.lower().endswith((".jpg", ".jpeg")), "Wrong file extention"
        img = Image.open(path)
    except (FileNotFoundError, PermissionError, UnidentifiedImageError, AssertionError) as error:
        print("Error: ", error)
        return (None)
    array = np.array(img)
    print("The shape of image is:", array.shape)
    return array
