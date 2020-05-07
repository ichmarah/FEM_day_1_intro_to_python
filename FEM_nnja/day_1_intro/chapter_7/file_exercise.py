# Using the open() keyword on its own is frowned upon, because it won’t automatically close any resources you might open. Even if you call the close() keyword yourself, there’s no guarantee your program won’t crash, leaving important resources dangling. It’s safer to open files inside a context using the with keyword. Once your code exits the scope of the context, your file is automatically closed.

import json


def main():
    with open("FEM_nnja/chapter_7/cities.json") as cities_files:
        try:
            cities_data = json.load(cities_files)

            print("Largest cities in the US by population:")
            # Print the data neater with enumarate() that prints a tuple of index and entry
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")
        except json.decoder.JSONDecodeError as error:
            print(f"\t {error}")
        print("The file is now closed")


if __name__ == "__main__":
    main()
