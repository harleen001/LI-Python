from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

try:
    driver.get("https://the-internet.herokuapp.com/")
    
    # 1. Use JavaScript to scroll to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print("Scrolled to bottom.")

    # 2. Use JavaScript to highlight an element (the footer)
    footer = driver.find_element(By.ID, "page-footer")
    driver.execute_script("arguments[0].style.border='5px solid red'", footer)
    
    # 3. Take a screenshot of the result
    driver.save_screenshot("highlight_test.png")
    print("Screenshot saved as highlight_test.png")

except Exception as e:
    print(f"Error: {e}")