# from load_image import ft_load
from PIL import Image
import numpy as np

def print_image(array: np.array):
    Image.fromarray(array).show()

def get_average_rgb(array: np.array):
    """
    return a 2d array with the average value of red, green, blue value in
    a 3d rgb array
    """
    average_array = np.empty((array.shape[0], array.shape[1]))
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            average = 0
            for k in range(array.shape[2]):
                average += array[i, j][k]
            average = average // array.shape[2]
            average_array[i, j] = average
    return (average_array)
            
            
def ft_invert(array: np.array):
    """Inverts the color of the image received"""
    inverted = array.copy()
    inverted = 255 - inverted
    print_image(inverted)

def ft_red(array: np.array):
    average_colors = get_average_rgb(array)
    red = array.copy()

    for i in range(average_colors.shape[0]):
        for j in range(average_colors.shape[1]):
            red[i, j] = [average_colors[i, j], 0, 0]
    print_image(red)

def ft_green(array: np.array):
    average_colors = get_average_rgb(array)
    green = array.copy()

    for i in range(average_colors.shape[0]):
        for j in range(average_colors.shape[1]):
            green[i, j] = [0, average_colors[i, j], 0]
    print_image(green)

def ft_blue(array: np.array):
    average_colors = get_average_rgb(array)
    blue = array.copy()

    for i in range(average_colors.shape[0]):
        for j in range(average_colors.shape[1]):
            blue[i, j] = [0, 0, average_colors[i, j]]
    print_image(blue)

def ft_grey(array: np.array):
    average_colors = get_average_rgb(array)
    grey = array.copy()

    for i in range(average_colors.shape[0]):
        for j in range(average_colors.shape[1]):
            grey[i, j] = [average_colors[i, j], average_colors[i, j], average_colors[i, j]]
    print_image(grey)

def ft_yellow(array: np.array):
    average_colors = get_average_rgb(array)
    yellow = array.copy()

    for i in range(average_colors.shape[0]):
        for j in range(average_colors.shape[1]):
            yellow[i, j] = [average_colors[i, j], 0, average_colors[i, j]]
    print_image(yellow)