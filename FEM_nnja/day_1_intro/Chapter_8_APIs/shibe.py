import requests
from pprint import pprint

api_url = "http://shibe.online/api/shibes?count=1"
api_url_params = "http://shibe.online/api/shibes"

# Provide the amount as parameters of URLS to request
params = {
    "count": 10
}

# Fetch data and store result in response variable
response = requests.get(api_url)
# Fetch data with parameter and store result in response_params variable
response_params = requests.get(api_url_params, params=params)

# Provide the data to be human readable by converting it to JSON format
response_json = response.json()
response_params_json = response_params.json()

# Requesting non-existing data in the API
bad_request = requests.get("http://shibe.online/api/BAD_DATA")

# Print response status by using method status_code() request built-in library
print(f"This is the status code of the API URL: {response.status_code} \n")
# Prints --> This is the status code of the API URL: 200

print(f"One dog picture URL: {response_json} \n")
# Prints --> One dog picture URL: ['https://cdn.shibe.online/shibes/43f3a1dbc7c810ca69e7d3dddcae8a94a2be4086.jpg']

# Print bad data response
print(
    f"Status code when requested data does not exist: {bad_request.status_code} \n")

# Print the URLs
pprint(f"The 10 URLs: {response_params_json}")
# Prints -->
# ('The 10 URLs: '
#  "['https://cdn.shibe.online/shibes/d436b97f374c0caca93b279317a2d95f16b7d86a.jpg', "
#  "'https://cdn.shibe.online/shibes/75a4b7ece22193b6db810ccf18d0e6b01748820a.jpg', "
#  "'https://cdn.shibe.online/shibes/05be3fc7620ac460a08a49008e47a1f4c234dd97.jpg', "
#  "'https://cdn.shibe.online/shibes/c30a82a47e3e7e0d1b39ff1406289ee93330caaa.jpg', "
#  "'https://cdn.shibe.online/shibes/1f49329562207a540708cbcc77c4977e133aca58.jpg', "
#  "'https://cdn.shibe.online/shibes/f7f6f3c53693ca4fc6e12ad8f0acaf89264b9a8f.jpg', "
#  "'https://cdn.shibe.online/shibes/1cb298abd56991f703ae916f624963f8a4c116b8.jpg', "
#  "'https://cdn.shibe.online/shibes/d8c72c4ce25367119898f584b555e4d6fc42f3b9.jpg', "
#  "'https://cdn.shibe.online/shibes/0881d5d0096b596f3958248646c7a0cdec22f8cb.jpg', "
#  "'https://cdn.shibe.online/shibes/f98bd3f81b40fca0bcfb6c055bda2ef244e5d290.jpg']")
