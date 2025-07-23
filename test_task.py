import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://todo-react-rouge.vercel.app/")
wait = WebDriverWait(driver, 10)
#add
todo_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
todo_input.send_keys("new item")
todo_input.send_keys(Keys.ENTER)
time.sleep(2)
# mark
complete_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.complete-btn")))
complete_button.click()
time.sleep(2)
# delete
trash_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.trash-btn")))
trash_button.click()
time.sleep(3)
driver.quit()