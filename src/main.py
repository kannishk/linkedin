from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import dotenv_values

# Config Stuff
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

def setup_driver(brave_path: str):
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    return webdriver.Chrome(chrome_options=option)

# Configuring driver.
config = dotenv_values(".env")
# driver = setup_driver(BRAVE_PATH)

# # Visiting linkedin's login page.
# driver.get("https://www.linkedin.com/uas/login")
# driver.implicitly_wait(3)

# # filling the form.
# elementID = driver.find_element(By.ID, 'username')
# elementID.send_keys(config['USERNAME'])
# elementID = driver.find_element(By.ID, 'password')
# elementID.send_keys(config['PASSWORD'])
# elementID.submit()

# otp = input(">> Enter the OTP: ")
from linkedin_api import Linkedin
import json

# https://www.linkedin.com/search/results/people/?geoUrn=%5B%22106442238%22%2C%22115918471%22%5D&keywords=blockchain%20developer&origin=FACETED_SEARCH&position=0&searchId=9f344935-37cc-4893-8c83-b89d034b338c&sid=!%3BF
# 106442238
api = Linkedin(config['USERNAME'], config['PASSWORD'])

res = api.search_people(
    # keyword_title=['blockchain developer'],
    keywords="blockchain developer",
    regions=['115918471', '106442238']
)
# res = api.search()
# print(json.dump(api.get_profile("pallavi-chauhan-ba6a99193"), open("./person.json", "w")))
# print(json.dump(api.get_profile("pallavi-chauhan-ba6a99193"), open("./pallavi.json", "w")))
with open("people.json", "w") as file:
    json.dump(res, file)
print("Length: ", len(res))
# https://www.linkedin.com/search/results/all/?keywords=blockchain%20developer&origin=AUTO_COMPLETE&position=4&searchId=e7b0f139-2776-4af0-b2d7-76426582e89f&sid=V%3AI


