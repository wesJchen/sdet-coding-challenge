import time
from selenium.webdriver.common.by import By

from page_objects.elements import PageElements
from page_methods.browser_methods import Webscraper


class Main:

    def __init__(self):
        self.current_group = None

    def process_solution(self):
        entry = Webscraper()
        entry.navigate_to_url(PageElements.base_url)

        gold_bars_page_element = entry.driver.find_element(By.XPATH,PageElements.gold_options) #Scrape the gold bar elements options
        num_gold_bars = len(gold_bars_page_element.find_elements(By.XPATH,'./*')) #Get the number of gold bars options on page
        self.current_group = list(range(0,num_gold_bars)) #Create the current group to test through

        while (len(self.current_group)) > 1:
            half_length = len(self.current_group) // 2
            grouped_array = [self.current_group[i:i+half_length] for i in range(0,len(self.current_group),half_length)]

            for index, gold in enumerate(grouped_array[0]):
                entry.left_basket(str(gold), index)
            time.sleep(1)
            for index, gold in enumerate(grouped_array[1]):
                entry.right_basket(str(gold), index)
            time.sleep(1)

            entry.click_weigh()
            results = entry.get_weigh_results()
            time.sleep(3)

            for check in results:
                if "=" in check:
                    self.current_group = grouped_array[2]
                elif "<" in check:
                    self.current_group = grouped_array[0]
                else:
                    self.current_group = grouped_array[1]
            
            entry.click_reset()
            time.sleep(3)

        for x in self.current_group:
            entry.select_fake_bar(str(x))
        time.sleep(3)
            
        entry.close_browser()


if __name__ == "__main__":
    solution_instance = Main()
    solution_instance.process_solution()