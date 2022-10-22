from selenium.webdriver.support import select
from selenium.webdriver.common.keys import Keys

class Actions:
    def __init__(self,driver):
        self.driver = driver

    def click(self,element):
        element.click()

    def sendKeys(self,inputfield, value):
        inputfield.send_keys(value)

    def selectFromDD(self,dropdown, value):
        ddelement = select(dropdown)
        ddelement.select_by_value(value)

    def getText(self,element):
        return element.text