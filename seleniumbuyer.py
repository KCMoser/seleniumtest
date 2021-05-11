
import subprocess
import pyautogui
import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pathlib import Path
from retrying import retry

logging.basicConfig(filename='tracking.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Read in confidential data and convert to text, stripping out newline char in variables
f=open('data.txt','r')
#txt = f.read().split('\n')
usr = f.readline().split('\n')
usr = usr[0]
pwd = f.readline().split('\n')
pwd = pwd[0]

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
time.sleep(1)
driver.find_element(By.ID, "ap_email").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.ID, "ap_password").send_keys(pwd)
time.sleep(1)
driver.find_element(By.ID, "ap_password").send_keys(Keys.ENTER)

logging.info('retry starts')
# Here I need to insert the search for the buy button loop with page refresh
@retry(wait_fixed=2500)         # Retrying, pausing every 2.5 seconds
def seeker():
  print('checking begins')
  logging.info('retrying')
  l= driver.find_element(By.ID, "submit.buy-now")
  #l= driver.find_element(By.ID, "a-autoid-0-announce")
  print("This button is not on the page")
seeker()

logging.info('retry completes')
print('Button Found, code continuing')
#driver.refresh()
#time.sleep(2)

#pyautogui.moveTo(1561, 966)
#pyautogui.sleep(2)
#pyautogui.click()
#time.sleep(3)
#pyautogui.click(2692, 553)

