# ============================ Comprehensions  ============================
# 1.  Create a list of only even numbers between 0 and 100 using a list comprehension.
# 2. Then, use a comprehension to create a dictionary where the keys are the even numbers from your list, and the values are random integers between 0 and 100 (hint: try random.randint(min, max)).
# 3. Finally, use a comprehension to create a set of every unique value from the above dictionary.

# 1
from random import randint
even_list = [num for num in range(0, 100) if (num % 2 == 0)]
print(f"Even list: {even_list}")
# Even list: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

# 2
my_dict = {num: randint(0, 100) for num in even_list}
print(f"Dictionary: {my_dict}")
# Dictionary: {0: 77, 2: 98, 4: 76, 6: 29, 8: 53, 10: 34, 12: 43, 14: 49, 16: 94, 18: 80, 20: 20, 22: 29, 24: 71, 26: 53, 28: 31, 30: 54, 32: 15, 34: 37, 36: 90, 38: 54, 40: 49, 42: 89, 44: 44, 46: 16, 48: 89, 50: 95, 52: 74, 54: 20, 56: 22, 58: 22, 60: 77, 62: 23, 64: 6, 66: 5, 68: 87, 70: 94, 72: 99, 74: 1, 76: 94, 78: 99, 80: 91, 82: 72, 84: 24, 86: 85, 88: 97, 90: 98, 92: 7, 94: 40, 96: 36, 98: 10}

# 3
unique_values = {num for num in my_dict.values()}
print(f"Unique values: {unique_values}")
# Unique values: {1, 5, 6, 7, 10, 15, 16, 20, 22, 23, 24, 29, 31, 34, 36, 37, 40, 43, 44, 49, 53, 54, 71, 72, 74, 76, 77, 80, 85, 87, 89, 90, 91, 94, 95, 97, 98, 99}


# ============================ Slicing  ============================
# 4. Make a list of numbers between 0 and 100, then try making a list of even numbers between 30 and 70, by taking a slice from the first list.
# 5. Then, make a new list in the reverse order.

# 4.
new_list = [num for num in range(0, 100)]
print(f"New list: {new_list}")
my_slice = new_list[30:70:2]
print(f"Slice: {my_slice}")
# # New list: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
# Slice: [30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68]


# 5
reverse_list = my_slice[::-1]
print(f"Reverse list: {reverse_list}")
# Reverse list: [68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30]


# ============================ zip  ============================
# 6. Make a list of all the names you can think of, called “names”. Make a second list of numbers, called “scores”, using a list comprehension and random.randint(min, max) as before. Use the first list in your comprehension to make it the same length. Then, use zip() to output a simple scoreboard of one score per name.

# 6
names = ["Josh", "Nik", "Nina", "Payo", "Lola"]
# The length of scores will be same as names
scores = [randint(0, 100) for name in names]

for (name, score) in zip(names, scores):
    print(f"🗣 {name} has a score of {score} points! 🎉")
# Prints out:
# 🗣 Josh has a score of 49 points! 🎉
# 🗣 Nik has a score of 81 points! 🎉
# 🗣 Nina has a score of 28 points! 🎉
# 🗣 Payo has a score of 44 points! 🎉
# 🗣 Lola has a score of 93 points! 🎉
