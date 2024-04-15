from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
try:
    bmi = give_bmi(height, weight)
except AssertionError:
    print("Assertion error: lists are not valid")
    exit(0)
print(bmi, type(bmi))
try:
    print(apply_limit(bmi, 26))
except TypeError:
    print("Type error: the list is not valid")
