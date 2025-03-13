# Import the requests library
import requests

# Send a GET request to the GitHub API
response = requests.get("https://api.github.com")

# Print the status code of the response
print("Status Code:", response.status_code)

# Print the response data in JSON format
print("Response Data:", response.json())