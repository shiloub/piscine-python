from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array :
    img = Image.open(path)
    array = np.array(img)
    print("The shape of image is:", array.shape)
    print(array)
    del(img)
    return array