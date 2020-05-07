# When checking if key or value exists in a dictionary, we can use the get() method in order to prevent an error message (which breaks the code)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
# eggs['color'] will give an error

print(eggs)
# gives 8. If there was no 'age, the fallback default value will be added to the dictionary if the key doesn't exist in dictionary --> age': 0
print(eggs.get('age', 0))

# ===============================================

# Opposite of get() method: setdefault() method: to set a value in dict for a certain key only if that key is not already set
eggs.setdefault('color', 'orange')
print(eggs)  # now 'color': 'orange' is added to the dict.
# If we call setdefault('color', 'orange'), nothing happens becuase color is already set.

