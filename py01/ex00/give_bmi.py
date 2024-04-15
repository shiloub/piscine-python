

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    assert len(height) == len(weight)
    bmis = []
    for meters, kilograms in zip(height, weight):
        assert isinstance(meters, (int, float)) and isinstance(kilograms,
                                                               (int, float))
        bmis.append(kilograms / (meters ** 2))
    return (bmis)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bools = [indice > limit for indice in bmi]
    return bools
