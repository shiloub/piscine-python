from PIL import Image, UnidentifiedImageError
import numpy as np


def ft_load(path: str):
    try:
        img = Image.open(path)
    except (FileNotFoundError, PermissionError, UnidentifiedImageError) as error:
        print("Error: ", error)
        return (None)
    array = np.array(img)
    print("The shape of image is:", array.shape)
    return array
#your code 