#!/usr/bin/env python3

# Cspell: words wttr
# Cspell: ignore REQUES winddir windspeed

"""
     REQUES...R_DEMO.PY INFO HEADER
----------------------------------------
NAME: requests_weather_demo.py
VERSION: 0.1.0
DESCRIPTION:
  A program using `requests` to query
  the wttr.in API and print the data
  it gets.
AUTHOR: Aksel Rasmussen
REQUIREMENTS:
- requests /Python library, used for\\
           \\ making requests.       /
- jq /Shell command, used for demos\\
     \\ at the bottom of the file.  /
----------------------------------------
Foreword to those reading this file:
This file is kinda cool and I really
hope I've a) made it understandable and
b) made it work well. Thank you for your
time.
"""

import requests

# TODO: Check if these are appropriate
VALID_CHARS = \
    'abcdefghijklmnopqrstuvwxyz' \
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
    '0123456789+-_%,.!'
INVALID_CHARS = \
    '/?=& $\\<>'

def escape_for_url(string: str) -> str:
    """Escapes a string for use in a section of a URL

    Primarily removes `/`, `?`, `=`, and `&` from a string.
    Behavior is not well described in this docstring.

    Takes a single string argument, and returns a string.
    """
    out = ''
    for ch in string:
        if ch == ' ':
            ch = '+'

        # NOTE: not sure weather to allowlist or denylist here

        #if ch in VALID_CHARS:
        #    out += ch
        if ch not in INVALID_CHARS:
            out += ch
    return out

def get_weather(city: str) -> dict:
    """Get the weather in a given location or city.

    Uses wttr.in and the requests library to find the
    current weather.

    Arguments:
    - city (str): The city or location to get the
      weather for.

    Returns:
    A dict representing the weather in wttr.in's `j2` format.

    Raises:
    - ValueError if `city` is an image filename.
    - Some form of HTTPError if the request fails.
    """
    # Avoid images. (wttr.in has special functionality we wanna
    # avoid here)
    if (city[:-4]
        in [
            '.png',
            '.jpg',
            '.gif',
            '.webp'
        ]):
        raise ValueError("Image requests break this function")

    # Make a GET
    r = requests.get(
        'https://wttr.in/'+ # << Base URL
        escape_for_url(city)+ # << Location
        '?format=j2' # << Json format
        #'?format=j1' # << extra verbose (hourly) Json format
        , timeout=30
    )

    # Ensure request returned properly
    r.raise_for_status()

    # Get the JSON and return it
    out = r.json()
    assert isinstance(out, dict)
    return out

if __name__ == "__main__":
    # loc = "LAX"           # << wttr.in supports airports btw =)
    # loc = "Chicago"       # << wttr.in supports cities too ;)
    # loc = "192.186.300.5" # << wttr.in will get this IP's location's weather XX(
    # loc = "@github.com"   # << wttr.in will get Github's IP's location's weather ^o^
    # loc = ""              # << wttr.in will guess your location by IP :-)
    print("Location to get weather for (Enter to guess your current location):")
    loc = input("> ")
    w = get_weather(loc)
    #print(w)
    #print(w["current_condition"])

    # Use the commands at the bottom of the file to help understand
    # what's going on.
    print(f"The time is ~{w['current_condition'][0]['observation_time']} on "
          f"{w['weather'][0]['date']}.")
    print(f"The current weather is {w['current_condition'][0]['weatherDesc'][0]['value']}.")
    print(f"The temperature is {w['current_condition'][0]['temp_F']}℉.")
    print(f"The temperature feels like {w['current_condition'][0]['FeelsLikeF']}°F.")
    print(f"The UV Index is {w['current_condition'][0]['uvIndex']}.")
    print(f"The wind is heading {w['current_condition'][0]['winddir16Point']} "
          f"and moving at {w['current_condition'][0]['windspeedMiles']} MPH.")
    print(f"You are near {w['nearest_area'][0]['areaName'][0]['value']}.")


# Useful commands (requires `jq`):
# `curl 'wttr.in/LAX?format=j2' 2>/dev/null | jq -C | less`
#   ^<< will output the weather in LAX in json format
# `curl 'wttr.in/LAX?format=j2' 2>/dev/null | jq -C | less`
#   ^<< will output the weather in your current location in json format
# `curl 'wttr.in'`
#   ^<< will output the weather in your current location fancily
