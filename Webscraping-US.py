import requests

url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

# Define a User-Agent to identify your browser/script
headers = {
    'User-Agent': 'MyPythonScraper/1.0 (contact@example.com)'
}

# Pass the headers into the get request
result = requests.get(url_link, headers=headers)

if result.status_code == 200:
    print(result.text)
else:
    print(f"Error: {result.status_code}")