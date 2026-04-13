import requests
from bs4 import BeautifulSoup

url_link = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

# Identifying yourself to Wikipedia's servers
headers = {
    'User-Agent': 'MyPythonScraper/1.0 (contact@example.com)'
}

# 1. Fetch the data
result = requests.get(url_link, headers=headers)

# 2. Check if the request was successful before parsing
if result.status_code == 200:
    # Use result.text to get the HTML content
    doc = BeautifulSoup(result.text, "html.parser")
    
    # 3. Print the prettified HTML
    print(doc.prettify())
else:
    print(f"Error: {result.status_code}")