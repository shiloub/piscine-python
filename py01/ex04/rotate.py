from load_image import ft_load
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def print_plt(array: np.array):
    plt.imshow(array, cmap="gray")
    # plt.__name__ = "blou"
    plt.show()

def parse_params(array, start: tuple[int, int], end: tuple[int, int]):
    
    if (end is None):
        end = (len(array[0], len(array)))
    for (x, y) in [start, end]:
        assert x >= 0 and y >= 0
    x1, y1 = start
    x2, y2 = end

    xstart = x1 if x1 < x2 else x2
    xend = x1 if x1 > x2 else x2
    ystart = y1 if y1 < y2 else y2
    yend = y1 if y1 > y2 else y2

    return (xstart, xend, ystart, yend)


def rotate_array(array: np.array)-> np.array:
    # assert len(array) == len(array[0])
    rotated = np.empty((len(array[0]), len(array)), dtype="int")
    for i in range(len(array)):
        for j in range(len(array[0])):
            rotated[j, i] = int(array[i, j])
    return rotated

def print_zoomed_bw_rotated(array: np.array, start = (0, 0), end = None):
    try:
        xstart, xend, ystart, yend = parse_params(array, start, end)
    except AssertionError as err:
        print(err)
        return
    array = array[ystart:yend, xstart:xend]
    bw = [] 
    new_row = []
    for row in array:
        new_row = []
        for pixel in row:
            new_row.append(int(pixel[0]) + int(pixel[1]) + int(pixel[2]))
        bw.append(new_row)
    bw = np.array(bw)
    bw = bw // 3
    print("The shape of image is:", bw.shape)
    print(bw)
    bw = rotate_array(bw)
    print("New shape after Transpose:", bw.shape)
    print(bw)
    print_plt(bw)

def main():
    pixels = ft_load("../animal.jpeg")
    print_zoomed_bw_rotated(pixels, (450, 100), (850, 500))


if __name__ == "__main__":
    main()

