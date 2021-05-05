# This script is for use with MS Surface 6 with 27" Sceptre external monitor driving InforLN

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time                                                                     # For script pauses
from pathlib import Path

# Grab logged in user home folder
hmefldr = str(Path.home())
# Set logged in users local folders
dirtouse = hmefldr + '\\documents\\'
dirtowrite = hmefldr + '\\desktop\\'
driver = webdriver.Chrome(dirtouse + "chromedriver.exe")
driver.get('https://login.salesforce.com/?ec=302&startURL=%2Fhome%2Fhome.jsp')
time.sleep(5)
print('Sleep stopped')
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys('')
driver.find_element(By.NAME, "pw").send_keys('')
driver.find_element(By.NAME, "Login").send_keys(Keys.ENTER)
print('login successful')
driver.find_element(By.NAME, "Reports").send_keys(Keys.ENTER)                   # Name is not reports
driver.find_element(By.ID, "157:0;p").send_keys('Am I in Search?')

time.sleep(5)
driver.quit()
