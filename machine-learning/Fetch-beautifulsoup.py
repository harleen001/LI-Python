#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint

# 1. Use the updated domain
url = 'https://www.ayush.nz/technology'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    print(f"Connecting to {url}...")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    
    my_data = []
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Updated Selector for the new structure
    # The new site structure uses different wrappers. 
    # Let's find all links that look like post entries.
    articles = soup.find_all('a', href=True)
    
    for article in articles:
        # Looking for the title inside the link (usually in a header tag)
        title_el = article.find(['h2', 'h3', 'h4', 'h5'])
        
        if title_el:
            title = title_el.get_text(strip=True)
            # Find the date or excerpt often located near the title
            # This is a broader search to ensure we catch the content
            parent = article.parent
            excerpt_el = parent.find('p')
            date_el = parent.find('small') or parent.find('time')

            my_data.append({
                "title": title, 
                "excerpt": excerpt_el.get_text(strip=True) if excerpt_el else "No excerpt found", 
                "pub_date": date_el.get_text(strip=True) if date_el else "No date found"
            })

    # Filter out empty or irrelevant matches
    my_data = [item for item in my_data if len(item['title']) > 5]

    pprint(my_data)

    # 3. Create the file
    with open('articles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "excerpt", "pub_date"])
        writer.writeheader()
        writer.writerows(my_data)

    print(f"\nSuccess! Created articles.csv with {len(my_data)} rows.")

except Exception as e:
    print(f"Error: {e}")