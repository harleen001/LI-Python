import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# --- 1. SETUP ---
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)

final_results = []

try:
    # --- 2. FETCH STAGE ---
    print("🚀 Stage 1: Fetching Quotes...")
    driver.get("https://quotes.toscrape.com")
    quotes = driver.find_elements(By.CLASS_NAME, "quote")[:3] # Limit to 3 for speed
    
    temp_data = []
    for q in quotes:
        temp_data.append({
            "Author": q.find_element(By.CLASS_NAME, "author").text,
            "Quote": q.find_element(By.CLASS_NAME, "text").text
        })

    # --- 3. SEARCH & TABLE STAGE ---
    print("🚀 Stage 2: Searching Authors and Building Report...")
    for item in temp_data:
        driver.get("https://www.bing.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(item['Author'])
        search_box.send_keys(Keys.ENTER)
        time.sleep(2) # Let results load
        
        # Get the snippet text from the first result
        try:
            snippet = driver.find_element(By.CSS_SELECTOR, "li.b_algo p").text
        except:
            snippet = "No summary found."

        final_results.append({
            "Author": item['Author'],
            "Quote": item['Quote'],
            "Search_Summary": snippet
        })

    # --- 4. EXPORT TO HTML TABLE ---
    df = pd.DataFrame(final_results)
    
    # Create a nice HTML file with basic styling
    html_content = f"""
    <html>
    <head>
        <title>Scraping Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }}
            table {{ border-collapse: collapse; width: 100%; background: white; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #0078d4; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h2>Selenium Automation Report</h2>
        {df.to_html(index=False)}
    </body>
    </html>
    """
    
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("\n✅ Pipeline Complete!")
    print(f"Check your folder for 'report.html' and open it in a browser.")

except Exception as e:
    print(f"❌ Error: {e}")