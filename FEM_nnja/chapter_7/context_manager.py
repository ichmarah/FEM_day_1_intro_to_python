# Context Manager  is like a wrapper around a block of code that depends on some resource. It’s a safer way of handling resources than, say, using open() and then remembering to close() later (and hoping your program doesn’t crash in between).

# json library is imported
# json data is downloaded from https://www.learnpython.dev/code/cities.json
# The relative path of the file should be used

import json
with open("FEM_nnja/chapter_7/cities.json") as cities_files:
    # Parse json data to readable text
    cities_data = json.load(cities_files)
    print(cities_data)
    # breakpoint() #is used to debug instead of print(). In terminal you can interact with it. Prompt starts with (Pdb)
    # Remove breakpoint() in production
    # e.g., city= cities_data[0] and then call the keys from that city

# Prints out:
# [{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, {'name': 'Philadelphia', 'pop': 1567442}]
