from selenium import webdriver
import time

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

try:
    # Open first site
    driver.get("https://www.google.com")
    print(f"Tab 1: {driver.title}")

    # Open a second tab using JavaScript
    driver.execute_script("window.open('https://www.bing.com');")
    
    # Get all window handles
    handles = driver.window_handles
    
    # Switch to the new tab (index 1)
    driver.switch_to.window(handles[1])
    time.sleep(2)
    print(f"Tab 2: {driver.title}")

    # Switch back to the first tab (index 0)
    driver.switch_to.window(handles[0])
    print(f"Back to Tab 1: {driver.title}")

except Exception as e:
    print(f"Error: {e}")