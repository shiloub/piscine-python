# print(filter.__doc__)

def is_odd(number):
    if (number % 2):
        return True
    return False

def non_returning_function():
    print("glouglou")

liste = [0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]

filtered_iterator = filter(is_odd, liste)

print(filtered_iterator)
for value in filtered_iterator:
    print(value)


# second_iterator = filter(None, liste)
# # third_it = filter(non_returning_function, liste)
# print(filtered_iterator)

# sec_filtered = list(second_iterator)
# filtered_list = list(filtered_iterator)
# # third_filtered = list(third_it)

# print(filtered_list)
# print(sec_filtered)
# print(third_filtered)