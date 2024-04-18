

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """take a list of height and a list of weight, and return a list
    of bmis"""
    assert len(height) == len(weight)
    bmis = []
    for meters, kilograms in zip(height, weight):
        assert isinstance(meters, (int, float)) and isinstance(kilograms,
                                                               (int, float))
        bmis.append(kilograms / (meters ** 2))
    return (bmis)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """take a list of bmis, and returs a list of bools if item is higher
    than limit"""
    bools = [indice > limit for indice in bmi]
    return bools
