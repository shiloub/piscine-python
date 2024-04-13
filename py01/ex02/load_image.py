from PIL import Image
import numpy as np


def ft_load(path: str) :# -> array: #(you can return to the desired format)
    img = Image.open(path)
    # shape = (img.height, img.width, len(img.mode))
    # print("The shape of image is:", shape)
    # pixels = []
    # row = []
    # for i in range (img.height):
    #     row = []
    #     for j in range(img.width):
    #         row.append(list(img.getpixel((j, i))))
    #     pixels.append(row)
    # return (pixels)
    array = np.array(img)
    print("The shape of image is:", array.shape)
    return array
#your code 