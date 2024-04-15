import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """print the shape of an array, slice it and print its new shape"""
    try:
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        new = np.array(family[start: end])
        print(f"My new shape is : {new.shape}")
        return (new.tolist())
    except ValueError as error:
        print("Error: ", error)
        return
