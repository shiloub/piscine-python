from load_image import ft_load
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def print_plt(array: np.array):
    plt.imshow(array, cmap="coolwarm_r")
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


def print_zoomed_bw(array: np.array, start = (0, 0), end = None):
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
    print("New shape after slicing:", bw.shape)
    print_plt(bw)


# def zoom_and_black_and_white(array: np.array) -> np.array :
#     zoomed = array[100: -300, 200: -200]
#     img = Image.fromarray(zoomed)
#     img = img.convert("L")
#     new_array = np.array(img)
    
#     return (new_array)


def main():
    pixels = ft_load("../animal.jpeg")
    # print(pixels)
    print_zoomed_bw(pixels, (450, 100), (850, 500))
    # print_plt(pixels)

    # zoomed_pixels: np.array = zoom_and_black_and_white(pixels)
    # print("--------------------------")
    # print("New shape after slicing:", zoomed_pixels.shape)
    # print(zoomed_pixels)
    # print_plt(zoomed_pixels)

    # plt.show()


if __name__ == "__main__":
    main()

