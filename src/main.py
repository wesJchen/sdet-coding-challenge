from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.elements import PageElements

import time

class Webscraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def navigate_to_url(self, url):
        self.driver.get(url)

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    entry = Webscraper()
    entry.navigate_to_url(PageElements.base_url)
    time.sleep(3)
    entry.close_browser()