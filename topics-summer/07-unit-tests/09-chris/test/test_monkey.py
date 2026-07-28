import json
from github_rest_api import is_valid_json, query_github


# =====================================================================
# PART 1: Basic Unit Tests (No Network Required)
# =====================================================================

def test_is_valid_json_with_valid_string():
    """Tests that a properly formatted JSON string returns True."""
    valid_data = '{"name": "pytest", "stars": 1000}'
    assert is_valid_json(valid_data) is True


def test_is_valid_json_with_invalid_string():
    """Tests that bad JSON or plain text returns False instead of crashing."""
    invalid_data = "Error: 404 - Not Found"
    assert is_valid_json(invalid_data) is False


# =====================================================================
# PART 2: The "Monkeytest" (Monkeypatching an API Call)
# =====================================================================

def test_query_github_success(monkeypatch):
    """
    Demonstrates 'Monkeypatching' (Mocking):
    We swap requests.get with a dummy function so our test runs fast,
    never hits rate limits, and works without an internet connection.
    """

    # 1. Create a fake response object that mimics requests.Response
    class FakeResponse:
        status_code = 200

        def json(self):
            # Simulated raw payload from GitHub API
            return {
                "items": [
                    {
                        "name": "cpython",
                        "full_name": "python/cpython",
                        "stargazers_count": 60000,
                        "html_url": "https://github.com/python/cpython",
                        "description": "The Python programming language",
                        "extra_field_to_ignore": "should be stripped out"
                    }
                ]
            }

    # 2. Define a dummy replacement for requests.get
    def fake_get(url, params):
        return FakeResponse()

    # 3. Use pytest's monkeypatch fixture to swap requests.get with fake_get
    monkeypatch.setattr("requests.get", fake_get)

    # 4. Call the function as normal
    result_json = query_github("https://api.github.com/fake_endpoint")

    # 5. Assertions: Check that filtering and formatting worked correctly
    assert is_valid_json(result_json) is True

    parsed_result = json.loads(result_json)
    assert len(parsed_result) == 1
    assert parsed_result[0]["name"] == "cpython"
    assert parsed_result[0]["stargazers_count"] == 60000
    # Ensure unneeded fields were filtered out
    assert "extra_field_to_ignore" not in parsed_result[0]


def test_query_github_api_failure(monkeypatch):
    """Bonus Monkeytest: Test how our code handles a 404 API error."""

    class FakeErrorResponse:
        status_code = 404
        text = "Not Found"

    def fake_get_error(url, params):
        return FakeErrorResponse()

    monkeypatch.setattr("requests.get", fake_get_error)

    result = query_github("https://api.github.com/fake_endpoint")
    assert result == "Error: 404 - Not Found"