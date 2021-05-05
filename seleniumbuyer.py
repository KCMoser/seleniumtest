
import subprocess
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pathlib import Path




# Grab logged in user home folder
hmefldr = str(Path.home())
# Set logged in users local variables
docs = hmefldr + '\\documents\\'
# Set Chrome driver for automation and opens browser
driver = webdriver.Chrome(docs + "chromedriver.exe")
# Maximize screen
driver.maximize_window()
# Opens web page
driver.get('https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62/ref=sr_1_7?dchild=1&keywords=ps5&qid=1620231120&sr=8-7')
time.sleep(3)
# Log me in
# Having trouble identifying the log in section, so switching to pyautogui :)
pyautogui.moveTo(1577, 178)
pyautogui.click()
driver.find_element(By.ID, "ap_email").send_keys(usr)
driver.find_element(By.ID, "ap_email").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.ID, "ap_password").send_keys(pwd)
driver.find_element(By.ID, "ap_password").send_keys(Keys.ENTER)

# Here I need to insert the search for the buy button loop with page refresh
# This element is on the page...
# 
driver.refresh()
time.sleep(2)

#pyautogui.moveTo(1561, 966)
#pyautogui.sleep(2)
#pyautogui.click()
#time.sleep(3)
#pyautogui.click(2692, 553)

