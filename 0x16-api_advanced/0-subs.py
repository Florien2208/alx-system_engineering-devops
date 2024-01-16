#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "MyApp/1.0.0 (by /u/YourRedditUsername)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return 0
    except (ValueError, AttributeError, KeyError) as e:
        print(f"Error parsing JSON response: {e}")
        return 0

# Example usage:
subreddit_name = "learnpython"
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit {subreddit_name} has {subscribers_count} subscribers.")

