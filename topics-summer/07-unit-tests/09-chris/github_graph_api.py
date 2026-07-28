import json
import requests
import os


def query_github_graphql(token):
    url = "https://api.github.com/graphql"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # We ask the server to search for Python repos, grab the first 4,
    # and strictly return ONLY the name, stars, and URL.
    query = """
    {
      search(query: "python sort:stars-desc", type: REPOSITORY, first: 4) {
        nodes {
          ... on Repository {
            name
            stargazerCount
            url
          }
        }
      }
    }
    """

    # GraphQL requests are always POST requests
    response = requests.post(url, headers=headers, json={"query": query})

    if response.status_code == 200:
        data = response.json()

        # Navigate the JSON response to grab our list of nodes (repositories)
        repos = data.get("data", {}).get("search", {}).get("nodes", [])

        # The data is already filtered over the network, we just format it cleanly
        filtered_items = [
            {
                "name": repo.get("name"),
                "stars": repo.get("stargazerCount"),
                "url": repo.get("url"),
            }
            for repo in repos
        ]

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
    # Best practice: Load your token from an environment variable
    # Export it in your terminal first: export GITHUB_TOKEN="your_token_here"
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

    if not GITHUB_TOKEN:
        print("Error: Please set the GITHUB_TOKEN environment variable.")
    else:
        return_json = query_github_graphql(GITHUB_TOKEN)

        if is_valid_json(return_json):
            print(return_json)
        else:
            print("Error: bad json returned from query_github_graphql().")