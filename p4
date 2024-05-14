from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = driver.find_element(By.NAME, "q")

    def search(self, text):
        self.search_box.send_keys(text)
