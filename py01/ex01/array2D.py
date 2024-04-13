import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        array = np.array(family)
        print(f"My shape is : {array.shape}")
        # print(array)
        new = np.array(family[start: end])
        print(f"My new shape is : {new.shape}")
        return (new.tolist())
    except ValueError as error:
        print("Error: ", error)
        return