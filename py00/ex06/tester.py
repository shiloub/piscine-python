from ft_filter import ft_filter


def is_odd(number):
    """return true if number is odd"""
    if (number % 2):
        return True
    return False


def is_color(str):
    """return true if str is a color"""
    colors = ["blue", "orange", "red", "green",
              "black", "white", "purple", "yellow"]
    if (str in colors):
        return True
    return False


def non_returning_function():
    """just print glouglou"""
    print("glouglou")


def main():
    """make some test comparing my function with the real filter function"""
    numbers = [1, 2, 4, 8, 3, 9, 18, 0, 7, 4, 13, 43, 78, 48, 93, 5, 9]
    empty = []
    words = ("nope", "black", "white", "orange", "pamplemousse",
             "vachekiri", "canon-a-saucisse", "purple")

    filtered = list(ft_filter(None, numbers))
    true = list(filter(None, numbers))
    print(filtered)
    print(true)
    print("------------------------------------")

    filtered = list(ft_filter(is_odd, numbers))
    true = list(filter(is_odd, numbers))
    print(filtered)
    print(true)
    print("------------------------------------")

    filtered = list(ft_filter(is_odd, empty))
    true = list(filter(is_odd, empty))
    print(filtered)
    print(true)
    print("------------------------------------")

    filtered = list(ft_filter(None, empty))
    true = list(filter(None, empty))
    print(filtered)
    print(true)
    print("------------------------------------")

    filtered = list(ft_filter(non_returning_function, empty))
    true = list(filter(non_returning_function, empty))
    print(filtered)
    print(true)
    print("------------------------------------")

    # filtered = list(ft_filter(non_returning_function, numbers))
    # true = list(filter(non_returning_function, numbers))
    # print(filtered)
    # print(true)
    # print("------------------------------------")

    filtered = list(ft_filter(is_color, words))
    true = list(filter(is_color, words))
    print(filtered)
    print(true)
    print("------------------------------------")
