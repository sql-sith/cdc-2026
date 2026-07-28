import requests
import json


def query_github(url):
    # GitHub API parameters: limit to 1 page containing 4 results
    params = {"per_page": 4, "page": 1}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract only the 5 key fields for each of the 4 repositories
        filtered_items = [
            {
                "name": repo.get("name"),
                "full_name": repo.get("full_name"),
                "stargazers_count": repo.get("stargazers_count"),
                "html_url": repo.get("html_url"),
                "description": repo.get("description"),
            }
            for repo in data.get("items", [])
        ]

        # Return formatted JSON string containing only filtered data
        return json.dumps(filtered_items, indent=4)
    else:
        return f"Error: {response.status_code} - {response.text}"


def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


if __name__ == "__main__":
    url = "https://api.github.com/search/repositories?q=python&sort=stars"
    return_json = query_github(url)
    if is_valid_json(return_json):
        print(return_json)
    else:
        print(f"Error: bad json returned from query_github().")
