#the idea of this test is just open the github and validate if the title if the same that i'm passing
import pytest
from selenium import webdriver
#com
def test_opengithub():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://github.com/dataengineerdeveloper')
    chrome_driver.maximize_window()
    title = "dataengineerdeveloper - GitHub"
    assert title ==chrome_driver.title
    print("Done")
    chrome_driver.close()
test_opengithub()