pages/example_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.some_element_locator = (By.ID, "some_element_id")

    def wait_for_element(self, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.some_element_locator)
            )
            return element
        except TimeoutException:
            return None

    def click_some_element(self):
        element = self.wait_for_element()
        if element:
            element.click()
        else:
            raise Exception("Element not found")
