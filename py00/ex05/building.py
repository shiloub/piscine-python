import sys


def main():
    """program that takes a single string argument and displays the sums
     of its upper-case characters, lower-case
     characters, punctuation characters, digits and spaces. If
     None or nothing is provided, the user is prompted to provide a string."""
    if len(sys.argv) == 1:
        try:
            str = input("What do i have to count ?\n")
        except EOFError:
            pass
    elif len(sys.argv) == 2:
        str = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return (0)
    # print(str, " <--")
    print(f"The text contains {len(str)} caracters:")
    upper_count = sum(1 for char in str if char.isupper())
    lower_count = sum(1 for char in str if char.islower())
    digit_count = sum(1 for char in str if char.isdigit())
    space_count = sum(1 for char in str if char.isspace())
    ponct = ",?;.:/!-_"
    ponctiation_count = sum(1 for char in str if char in ponct)
    print(upper_count, " upper letters")
    print(lower_count, " lower letters")
    print(ponctiation_count, " ponctuation marks")
    print(space_count, " spaces")
    print(digit_count, " digits")


if __name__ == "__main__":
    main()
