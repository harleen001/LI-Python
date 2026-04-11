import requests
from bs4 import BeautifulSoup
import csv
import os

# 1. Target URL
url = "https://quotes.toscrape.com/"
headers = {'User-Agent': 'Mozilla/5.0'}

try:
    # 2. Fetch and Parse
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Extract Data
    quote_elements = soup.select('.quote') 
    scraped_data = []

    for quote in quote_elements:
        scraped_data.append({
            'quote': quote.select_one('.text').get_text(strip=True),
            'author': quote.select_one('.author').get_text(strip=True),
            'tags': ", ".join([tag.get_text(strip=True) for tag in quote.select('.tag')])
        })

    # 4. Create the quotes.csv file
    filename = 'quotes.csv'
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['quote', 'author', 'tags'])
        writer.writeheader()
        writer.writerows(scraped_data)
        
    # Output confirmation and file path
    print(f"Success! '{filename}' has been created.")
    print(f"File location: {os.path.abspath(filename)}")

except Exception as e:
    print(f"An error occurred: {e}")