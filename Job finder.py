from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
from bidi.algorithm import get_display
import arabic_reshaper


path = r"C:\Users\t90na\Downloads\chromedriver_win32\chromedriver.exe"
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get('https://www.jobs.ps/')    #exploring a job website
implicitly_wait(30)
search_bar = driver.find_element(By.XPATH, value="//*[@id='main-wrapper']/header/div/form/div/input")
time.sleep(5)
search_bar.send_keys("Electrical Engineer")  # searching for a specific vacancy
mySearch = search_bar.send_keys(Keys.ENTER)

time.sleep(5)  
#get the entire element of the result comapny name, vacancy, date, location
search = driver.find_element(By.XPATH, '//*[@id="main-wrapper"]/div/div/div[2]/div[3]/div/div[2]/a[1]')
time.sleep(2)
#get the company names of results
search_results = driver.find_elements(By.CLASS_NAME, "list--cell--company ")
Companies_list = []
#listing company names
#adjusting arabic names to show properly
for result in search_results:
    Companies_list.append(get_display(arabic_reshaper.reshape(result.text)))
print(Companies_list, ": Company list")
#create json file of company names
myString = json.dumps(Companies_list)
jsonFile = open("companies.json","w")
jsonFile.write(myString)
jsonFile.close()
time.sleep(17)
#quiting the driver
driver.quit()
