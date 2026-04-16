import csv
import os
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_author_summary(driver, author_name):
    """Jumps directly to Wikipedia to grab a biography snippet."""
    try:
        # Direct URL jump is faster than searching
        search_url = f"https://en.wikipedia.org/wiki/{author_name.replace(' ', '_')}"
        driver.get(search_url)

        # Wait for the first real paragraph of text
        wait = WebDriverWait(driver, 5)
        summary_element = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".mw-parser-output > p:not(.mw-empty-elt)")
        ))
        
        # Clean up citation brackets [1][2] and trim length
        clean_text = re.sub(r'\[.*?\]', '', summary_element.text)
        return clean_text.strip()[:250] + "..." 
    except:
        return "Biography details currently unavailable."

def main():
    # --- 1. SETUP ---
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Speed hack: Disable images to load pages faster
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Edge(options=options)
    all_extracted_data = []

    try:
        # --- 2. FETCH STAGE (Scraping Quotes) ---
        print("🌐 Stage 1: Scrapping Quotes Website...")
        driver.get("https://quotes.toscrape.com")
        
        # Get the first 5 quotes to keep the pipeline snappy
        quote_containers = driver.find_elements(By.CLASS_NAME, "quote")[:5]
        
        raw_quotes = []
        for container in quote_containers:
            raw_quotes.append({
                "Author": container.find_element(By.CLASS_NAME, "author").text,
                "Quote": container.find_element(By.CLASS_NAME, "text").text
            })

        # --- 3. ENRICHMENT STAGE (Wikipedia) ---
        print("🔍 Stage 2: Enriching Data via Wikipedia...")
        cache = {} # Prevents duplicate searches for the same author
        
        for item in raw_quotes:
            author = item["Author"]
            if author not in cache:
                print(f"   -> Researching: {author}")
                cache[author] = get_author_summary(driver, author)
            
            all_extracted_data.append({
                "Author": author,
                "Quote": item["Quote"],
                "Bio": cache[author]
            })

        # --- 4. OUTPUT STAGE (CSV & HTML) ---
        df = pd.DataFrame(all_extracted_data)
        df.to_csv("pipeline_data.csv", index=False)
        
        # Generate the HTML Report
        html_file = "final_report.html"
        html_table = df.to_html(classes='report-table', index=False, escape=False)
        
        report_template = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', sans-serif; margin: 50px; background: #f0f2f5; }}
                h1 {{ color: #1a73e8; text-align: center; }}
                .report-table {{ width: 100%; border-collapse: collapse; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
                th {{ background: #1a73e8; color: white; padding: 15px; text-align: left; }}
                td {{ padding: 15px; border-bottom: 1px solid #eee; line-height: 1.5; color: #333; }}
                tr:hover {{ background: #f8f9fa; }}
            </style>
        </head>
        <body>
            <h1>🚀 Automation Intelligence Report</h1>
            {html_table}
        </body>
        </html>
        """
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(report_template)

        print(f"\n✅ SUCCESS! Pipeline completed.")
        print(f"Data saved to 'pipeline_data.csv' and '{html_file}'.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()