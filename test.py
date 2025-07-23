from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (make sure chromedriver is in PATH or specify path here)
driver = webdriver.Chrome()

# Step 1: Open the web application
driver.get("https://todo-react-rouge.vercel.app/")
driver.maximize_window()
time.sleep(2)

# Step 2: Add a new to-do item
todo_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
todo_input.send_keys("Test ToDo Item")
todo_input.send_keys(Keys.ENTER)
time.sleep(2)

# Step 3: Mark it as completed
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
checkbox.click()
time.sleep(1)

# Step 4: Delete the item
delete_button = driver.find_element(By.CSS_SELECTOR, ".delete-button")
delete_button.click()
time.sleep(2)

# Optional: Verify if the item was deleted
items = driver.find_elements(By.CSS_SELECTOR, ".todo-item")
assert len(items) == 0, "Item was not deleted!"

# Close the browser
driver.quit()
