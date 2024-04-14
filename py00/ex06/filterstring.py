import sys
from ft_filter import ft_filter


def main():
    """Program that take a string and a number as arguments.
    The string must be alnum with whitespaces allowed.
    The number must be over 0.
    Return all the words that contains more letter than the given number."""
    min = 0
    try:
        assert len(sys.argv) == 3
        min = int(sys.argv[2])
        assert min >= 0
        string = sys.argv[1]
        for char in string:
            assert (char.isalnum() or char.isspace())

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")
        exit(1)
    splited = string.split()
    # filtered = [word for word in splited if len(word) > min]
    filt = [word for word in ft_filter(lambda word: len(word) > min, splited)]
    # print(filtered)
    print(filt)


if __name__ == "__main__":
    main()
