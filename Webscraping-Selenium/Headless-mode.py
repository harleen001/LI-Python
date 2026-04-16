from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_argument("--headless") # Runs without opening a visible window

driver = webdriver.Edge(options=options)

print("Running in headless mode (no window will appear)...")
driver.get("https://www.python.org")
print(f"Successfully grabbed title in background: {driver.title}")

driver.quit()
print("Driver closed.")