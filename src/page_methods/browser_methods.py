from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from page_objects.elements import PageElements

class Webscraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Site interactions
    def navigate_to_url(self, url):
        self.driver.get(url)
    
    def close_browser(self):
        self.driver.quit()

    # Page element interactions
    def click_weigh(self):
        weigh_button = self.driver.find_element(By.XPATH,PageElements.weigh_button_xpath)
        weigh_button.click()

    def click_reset(self):
        reset_button = self.driver.find_element(By.XPATH,PageElements.reset_button_xpath)
        reset_button.click()

    def left_basket(self, gold_num:int, position:int):
        left_basket_element = self.driver.find_element(By.ID,PageElements.left_basket_id.format(position))
        left_basket_element.send_keys(gold_num)

    def right_basket(self, gold_num:int, position:int):
        right_basket_element = self.driver.find_element(By.ID,PageElements.right_basket_id.format(position))
        right_basket_element.send_keys(gold_num)
    
    def click_fake_bar(self, gold_num:int):
        fake_element = self.driver.find_element(By.XPATH, PageElements.fake_bar_solution_xpath.format(gold_num))
        fake_element.click()

    # Page element data
    def scrape_gold_elements(self):
        page_gold_elements = self.driver.find_element(By.XPATH,PageElements.gold_options_xpath)
        gold_elements_count = len(page_gold_elements.find_elements(By.XPATH,PageElements.gold_options_child_xpath))
        return gold_elements_count

    def get_weigh_results(self):
        result_element = self.driver.find_element(By.XPATH,PageElements.results_xpath)
        return result_element.text
    
    # Page element check condition
    def weigh_results_update(driver):
        return driver.find_element(By.XPATH, PageElements.results_xpath).text != PageElements.results_reset_text