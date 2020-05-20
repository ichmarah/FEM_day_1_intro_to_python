import requests

# Create dynamically the query to be included as parameter
def create_query(languages, min_stars=50000):
    # The space after the query word is necessary, 
    # otherwise error status code 422: Unprocessible Entry!
    query = f"stars:>{min_stars} "

    # Adds each language to the stars query above
    for language in languages:
        # The space after the query word is necessary, 
        # otherwise error status code 422: Unprocessible Entry!
        query += f"language:{language} "
    return query

def repo_most_stars(languages, sort="stars", order="desc"):
    # stars = "?q=stars:>50000" # --> this is hardcoded
    # github_api_url = f"https://api.github.com/search/repositories{stars}"
    
    github_api_url = f"https://api.github.com/search/repositories"
    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}

    response = requests.get(github_api_url, params=parameters)
    status_code = response.status_code
    
    # Check if rate limit has been reach (403) and check for any other erro
    if (status_code == 403):
        raise RuntimeError("Rate limit reached. Please wait a minute and try again")
    if (status_code != 200):
        raise RuntimeError(f"An error occured. HTTP Status Code was: {status_code}")
    else:
        #print(f"{response_json}")
        # Outcome --> {'total_count': 0, 'incomplete_results': False, 'items': []}
        response_json = response.json()
        return response_json["items"]


# Check if we are running the file directly
if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    items = repo_most_stars(languages)

    for item in items:
        name = item["name"]
        language = item["language"]
        stars = item["stargazers_count"]
    
        print(f"{name} is a {language} repo on Github with {stars} ⭐stars ⭐️.")
        # Outcome snippet -->
        # freeCodeCamp is a JavaScript repo on Github with 310563 ⭐stars ⭐️.
        # vue is a JavaScript repo on Github with 163528 ⭐stars ⭐️.
        # react is a JavaScript repo on Github with 148258 ⭐stars ⭐️.
        # bootstrap is a JavaScript repo on Github with 140581 ⭐stars ⭐️.
        # javascript is a JavaScript repo on Github with 95159 ⭐stars ⭐️.