import json

def main():
  cities_files = open("FEM_nnja/chapter_7/cities.json")
  cities_data = json.load(cities_files)
  print(cities_data)

if __name__ == "__main__":
    main()