from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Edge with 'detach' to keep it open
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

try:
    # This page has a button that starts a 5-second loading bar
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    
    # 1. Click the start button
    driver.find_element(By.CSS_SELECTOR, "#start button").click()
    
    # 2. SMART WAIT: Wait up to 10 seconds for the 'Hello World' text
    print("Waiting for dynamic content...")
    wait = WebDriverWait(driver, 10)
    finish_text = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    
    # 3. Retrieve the text
    print(f"Retrieved Dynamic Text: {finish_text.text}")

except Exception as e:
    print(f"Error occurred: {e}")