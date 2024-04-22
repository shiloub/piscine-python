def mean(values: tuple) -> float:
    return sum(values) / len(values)


def median(values: tuple) -> float:
    values = sorted(values)
    if (len(values) % 2):
        return values[len(values) // 2]
    return mean((values[(len(values) // 2) - 1], values[(len(values) // 2)]))


def quartile(values: tuple) -> list[float]:
    values = sorted(values)
    q1 = median(values[:(len(values) // 2) + len(values) % 2])
    q2 = median(values[-(len(values) // 2) - len(values) % 2:])
    return [float(q1), float(q2)]


def std(values: tuple) -> float:
    return (var(values) ** 0.5)


def var(values: tuple) -> float:
    squared_diffs = [(mean(values) - x) ** 2 for x in values]
    return mean(squared_diffs)


def ft_statistics(*args: any, **kwargs: any) -> None:
    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif value == "mean":
            print(f"mean : {mean(args)}")
        elif value == "median":
            print(f"median : {median(args)}")
        elif value == "quartile":
            print(f"quartile : {quartile(args)}")
        elif value == "std":
            print(f"std : {std(args)}")
        elif value == "var":
            print(f"var : {var(args)}")
