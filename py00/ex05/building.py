# import sys


# def main():
#     """program that takes a single string argument and displays the sums
#      of its upper-case characters, lower-case
#      characters, punctuation characters, digits and spaces. If
#      None or nothing is provided, the user is prompted to provide a string."""
#     if len(sys.argv) == 1:
#         try:
#             string = input("What do i have to count ?\n")
#             string += '\n'

#         except EOFError:
#                print("i got it")
#                exit()
#         #     pass
#     elif len(sys.argv) == 2:
#         string = sys.argv[1]
#     else:
#         print("AssertionError: more than one argument is provided")
#         return (0)
#     print(f"The text contains {len(string)} caracters:")
#     upper_count = sum(1 for char in string if char.isupper())
#     lower_count = sum(1 for char in string if char.islower())
#     digit_count = sum(1 for char in string if char.isdigit())
#     space_count = sum(1 for char in string if char.isspace())
#     ponct = ",?;.:/!-_"
#     ponctiation_count = sum(1 for char in string if char in ponct)
#     print(upper_count, " upper letters")
#     print(lower_count, " lower letters")
#     print(ponctiation_count, " ponctuation marks")
#     print(space_count, " spaces")
#     print(digit_count, " digits")


# if __name__ == "__main__":
#     main()


import sys
string = ''
# while ('\n' not in string):
#     char = sys.stdin.read(1)
#     if char == "":
#         print("oui")
#         break
#     string += char

print("oui")
string = sys.stdin.readline()
if string == "":
    print("ehoh")
print()

print(string)