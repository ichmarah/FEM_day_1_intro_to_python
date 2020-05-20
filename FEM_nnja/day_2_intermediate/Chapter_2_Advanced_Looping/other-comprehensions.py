# from list of tuples to dict
my_list = [(f"Player {num + 1}", num * num) for num in range(0, 10)]
print(my_list)
# Prints out:
# [('Player 1', 0), ('Player 2', 1), ('Player 3', 4), ('Player 4', 9), ('Player 5', 16), ('Player 6', 25), ('Player 7', 36), ('Player 8', 49), ('Player 9', 64), ('Player 10', 81)]

my_dict = {key: value for (key, value) in my_list}
print(my_dict)
# Prints out:
# {'Player 1': 0, 'Player 2': 1, 'Player 3': 4, 'Player 4': 9, 'Player 5': 16, 'Player 6': 25, 'Player 7': 36, 'Player 8': 49, 'Player 9': 64, 'Player 10': 81}
