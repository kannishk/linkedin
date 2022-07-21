# Auto LinkedIn

## How to setup

- Install dependencies

```bash
pipenv install
```

- Install chromedriver for your chrome version.
- Add it to the path.

## Requirements

![Requirements](https://i.ibb.co/MDcKQcn/image.png)

```py
from bs4 import BeautifulSoup
from selenium import webdriver

driver_path = '~/Desktop/chromedriver'

browser = webdriver.Chrome(executable_path=driver_path)

browser.get('https://www.linkedin.com/uas/login')

file = open('config.txt')
lines = file.readlines()

username = lines[0]
password = lines[1]

elementID = browser.find_element(by=id('username'))
elementID.send_keys(username)

elementID = browser.find_element(by=id('password'))
elementID.send_keys(password)

elementID.submit()
```

<!-- https://www.linkedin.com/in/pallavi-chauhan-ba6a99193/opportunities/job-opportunities/details/?profileUrn=urn%3Ali%3Afs%5Fnormalized%5Fprofile%3AACoAAC2LhG4BxE69cUzS%2Did2cz%2D3dI3xN5u39KM&trk=opento_nprofile_details -->

https://www.linkedin.com/in/pallavi-chauhan-ba6a99193/opportunities/job-opportunities/details/?profileUrn=urn:li:fs_normalized_profile:ACoAAC2LhG4BxE69cUzS-id2cz-3dI3xN5u39KM&trk=opento_nprofile_details

urn:li:fs_miniProfile:ACoAAC2LhG4BxE69cUzS-id2cz-3dI3xN5u39KM

https://www.linkedin.com/in/pallavi-chauhan-ba6a99193/opportunities/job-opportunities/details/?profileUrn=urn:li:fs_miniProfile:ACoAAC2LhG4BxE69cUzS-id2cz-3dI3xN5u39KM&trk=opento_nprofile_details
