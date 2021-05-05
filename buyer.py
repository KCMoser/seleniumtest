
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
# Open Chrome programmatically (causes control message in browser)
# apps = hmefldr + 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
# subprocess.Popen(apps)


pyautogui.moveTo(30, 1049)
pyautogui.sleep(2)
pyautogui.click()
pyautogui.moveTo(145, 346)
pyautogui.sleep(2)
pyautogui.click()
pyautogui.sleep(2)
pyautogui.typewrite('https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62/ref=sr_1_7?dchild=1&keywords=ps5&qid=1620231120&sr=8-7\n')

#pyautogui.moveTo(1561, 966)
#pyautogui.sleep(2)
#pyautogui.click()
#time.sleep(3)
#pyautogui.click(2692, 553)

# Set Chrome driver for automation
# driver = webdriver.Chrome(docs + "chromedriver.exe")