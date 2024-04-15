from array2D import slice_me
# import numpy as np
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

wrong = [[1.80, 78.4],
         [2.15, 102.7],
         [2.10, 98.5, 23],
         [1.88, 75.2]]

wrong2 = wrong = [[1.80, 78.4],
                  [2.15, "ho"],
                  [2.10, 98.5, 23],
                  [1.88, 75.2]]

wrong3 = family.copy()
wrong3.append("ines")
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
print(slice_me(family, 0, 17))
print()
print(wrong3)
print(slice_me(wrong, 0, 2))
print(slice_me(wrong2, 0, 2))
print(slice_me(wrong3, 0, 2))
# array = np.array([1, 2, "trois"], dtype=np.int64)
# print(array)
