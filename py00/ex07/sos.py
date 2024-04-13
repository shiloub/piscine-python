import sys


def translate(string) -> str:
    """take a string as argument and return its morse version"""
    NESTED_MORSE = {"A": ".- ", "B" :"-... ", "C": "-.-. ", "D": "-.. ",
            "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
            "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
            "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
            "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
            "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
            "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
            "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
            " ": "/ "}
    
    tab = [NESTED_MORSE[char.upper()] for char in string]
    encoded = "".join(tab)
    if len(encoded) and encoded[-1] == " ":
        encoded = encoded[:-1]
    return encoded


def isalnum_space(s):
    """Isalnum but not rejecting spaces"""
    for char in s:
        if not char.isalnum() and not char.isspace():
            return False
    return True
            


def main():
    """take a string as argument, and print its morse traduction"""
    try:
        assert len(sys.argv) == 2
        string = sys.argv[1]
        assert isalnum_space(string)

    except (AssertionError) as error:
        print("AssertionError: the arguments are bad")
        exit (1)
    print(translate(string))

if __name__ == "__main__":
    main()