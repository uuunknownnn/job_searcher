from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os

path = r"C:\Users\t90na\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(path)
os.environ['PATH'] += path
driver.get('https://www.jobs.ps/')    # exploring a job website
driver.implicitly_wait(20)
driver.maximize_window()

search_bar = driver.find_element_by_css_selector('input[class="header--search-input"]')
search_bar.send_keys("Electrical Engineer", Keys.ENTER)  # searching for a specific vacancy

time.sleep(5)  #wait till page completely loaded
# get the company names of results
search_results = driver.find_elements_by_css_selector(
    'a[class="list-3--title list-3--row"] div div[class="list--cell--company "]'
)

Companies_list = []
# listing company names

for result in search_results:
    Companies_list.append(result.text)
print(Companies_list, ": Company list")

# create json file of company names
myString = json.dumps(Companies_list)
jsonFile = open("companies.json", "w")
jsonFile.write(myString)
jsonFile.close()
print('Json file has been generated')
time.sleep(3)
# quiting the driver
driver.quit()
