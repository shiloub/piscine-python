from load_image import ft_load
import numpy as np
from matplotlib import pyplot as plt


def print_plt(array: np.array):
    """print the grey version image of a np.array"""
    plt.imshow(array, "binary_r")
    plt.show()


def parse_params(array, start: tuple[int, int], end: tuple[int, int]):
    """parse parametters"""
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


def print_zoomed_bw(array: np.array, start=(0, 0), end=None):
    """zoomed on an image, and print it grey"""
    try:
        xstart, xend, ystart, yend = parse_params(array, start, end)
    except AssertionError as err:
        print(err)
        return
    array = array[ystart:yend, xstart:xend]
    bw = np.round(np.mean(array, axis=2)).astype(np.uint8)
    bw = np.expand_dims(bw, axis=2)
    print("New shape after slicing:", bw.shape)
    print(bw)
    print_plt(bw)


def main():
    """load an image, print some informations about it.
    then print it grey and zoomed"""
    pixels = ft_load("../images/animal.jpeg")
    if pixels is None:
        print("Error loading the file")
        return (1)
    print(pixels)
    print_zoomed_bw(pixels, (450, 100), (850, 500))


if __name__ == "__main__":
    main()
