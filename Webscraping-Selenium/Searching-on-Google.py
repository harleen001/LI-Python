from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Setup Options for Stability and Stealth
edge_options = Options()

# KEEP BROWSER OPEN: This prevents the window from closing when the script ends
edge_options.add_experimental_option("detach", True)

# STEALTH: Hide the "I am a bot" flags
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_experimental_option('useAutomationExtension', False)

# 2. Initialize the Edge Driver
driver = webdriver.Edge(options=edge_options)

try:
    # 3. Navigate to Google
    driver.get("https://www.google.com")
    
    # Locate the search bar
    search_box = driver.find_element(By.NAME, "q")
    
    # 4. Human-like Interaction
    search_box.send_keys("What day is today")
    time.sleep(1) # Small pause to look human
    search_box.send_keys(Keys.ENTER)
    
    print("Success! The browser should remain open for you to see.")

except Exception as e:
    print(f"An error occurred: {e}")

