from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromeOptions = Options()
chromeOptions.add_argument("--user-data-dir=C:\\Users\\dhiraj.suvarna\\AppData\\Local\\Google\\Chrome\\User Data")
# chromeOptions.add_argument(r"--profile-directory=Profile 1")

driver = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", options=chromeOptions)

# driver.get("http://www.python.org")
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# driver.close

# driver.get("https://stackoverflow.com/")

driver.get("https://www.myhcl.com")
loadedPageTitle = driver.title
print(f"Page Title: {loadedPageTitle}")

if loadedPageTitle  == "Covid":
    submitBtn = driver.find_element_by_id("btnSubmitGood")
    submitBtn.click()

searchBox = driver.find_element_by_id("txtSearch")
value = searchBox.get_attribute("value")
print(f"search box text: {value} ")

searchBox.send_keys("itime")

itimeLocator = (By.XPATH, '//*[@id="ui-id-12"]/table/tbody/tr/td/a')
itimeElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(itimeLocator))
itimeElement.click()
#driver.close()