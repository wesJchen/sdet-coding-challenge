from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.elements import PageElements

class Webscraper:

    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def navigate_to_url(self, url):
        self.driver.get(url)

    def click_weigh(self):
        weigh_button = self.driver.find_element(By.XPATH,PageElements.weigh_button_xpath)
        weigh_button.click()

    def click_reset(self):
        reset_button = self.driver.find_element(By.XPATH,PageElements.reset_button_xpath)
        reset_button.click()

    def left_basket(self, gold_num:str, position:int):
        left_basket_element = self.driver.find_element(By.ID,f"left_{position}")
        left_basket_element.send_keys(gold_num)

    def right_basket(self, gold_num:str, position:int):
        right_basket_element = self.driver.find_element(By.ID,f"right_{position}")
        right_basket_element.send_keys(gold_num)

    def get_weigh_results(self):
        result_element = self.driver.find_element(By.ID,"reset")
        yield result_element.text

    def select_fake_bar(self, gold_num:str):
        fake_element = self.driver.find_element(By.XPATH, f'//*[@id="coin_{gold_num}"]')
        fake_element.click()

    def close_browser(self):
        self.driver.quit()