import sys

if (len(sys.argv) > 2):
    print("AssertionError: more than one argument is provided")
    exit(0)

try:
    number = int(sys.argv[1])
except ValueError:
    print("AssertionError: argument is not an integer")
    exit(0)
if (number % 2):
    print("I'm odd")
else:
    print("I'm even")