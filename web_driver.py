web_driver.py
# utils/web_driver.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

class WebDriver:
    @staticmethod
    def get_driver():
        options = Options()
        options.add_argument("--start-maximized")
        service = ChromeService(executable_path="path/to/chromedriver")
        
