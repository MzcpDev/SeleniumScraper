from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys

# Mac
driver = webdriver.Chrome(executable_path="./chromedriver") 

# windows
#driver = webdriver.Chrome(executable_path="C:\chromedriver.exe") 


### Access Website 
driver.get("https://www.google.com/")

# Input Text 
driver.find_element_by_id("ID").send_keys("strings")
# Get Text
driver.find_element_by_id("ID").text
# Get Atttribute
driver.find_element_by_id("ID").get_attribute("value")
# Title
driver.title
# Get source
driver.page_source