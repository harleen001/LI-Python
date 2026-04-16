from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)

try:
    driver.get("https://the-internet.herokuapp.com/iframe")

    # Switch into the iframe using its ID
    driver.switch_to.frame("mce_0_ifr")

    # Locate the text area inside the iframe
    editor = driver.find_element(By.ID, "tinymce")
    editor.clear()
    editor.send_keys("Hello from inside the iframe!")
    print("Typed inside the iframe.")

    # Switch back to the main document to click page-level links
    driver.switch_to.default_content()
    print("Back to main page content.")

except Exception as e:
    print(f"Error: {e}")