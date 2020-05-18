figures = ["Circle", "Square", "Triangle"]
colors = ["blue", "red", "green"]

# Iterate over both variables simultaneously
for figure, color in zip(figures, colors):
    print(f"{figure} has the color of {color}")
# Prints out:
# Circle has the color of blue
# Square has the color of red
# Triangle has the color of green

# Create a dict from a zip
my_dict = dict(zip(figures, colors))
print(my_dict)
# Prints out:
# {'Circle': 'blue', 'Square': 'red', 'Triangle': 'green'}
