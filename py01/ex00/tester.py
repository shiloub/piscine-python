from give_bmi import give_bmi, apply_limit

height = [1.67, 1.15]
weight = [53, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
# need to check errors