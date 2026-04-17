from selenium import webdriver

# Switch from Chrome to Edge
driver = webdriver.Edge() 

driver.get("https://www.google.com")
print(f"Success! The title is: {driver.title}")

#driver.quit()