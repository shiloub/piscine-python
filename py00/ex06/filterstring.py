import sys
from ft_filter import ft_filter

def main():
    min = 0
    try:
        assert len(sys.argv) == 3
        min = int(sys.argv[2])
        assert min >= 0
        string = sys.argv[1]

    except (AssertionError, ValueError) as error:
        print("AssertionError: the arguments are bad")
        exit (1)
    
    splited = string.split()
    filtered = [word for word in splited if len(word) > min]
    filtered2 = [word for word in ft_filter(lambda word: len(word) > min, splited)]
    print(splited)
    print(filtered)
    print(filtered2)
    

if __name__ == "__main__":
    main()