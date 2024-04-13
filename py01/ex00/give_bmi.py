import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmis = []
    for meters, kilograms in zip(height, weight):
        bmis.append(kilograms / (meters ** 2))
    return(bmis)
#your code here
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bools = []
    for indice in bmi:
        if (indice > limit):
            bools.append(True)
        else:
            bools.append(False)
    return bools