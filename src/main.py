import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

from page_objects.elements import PageElements
from src.page_methods.browser_methods import Webscraper

class Main:
    # Defined constant variables
    SHORT_SLEEP_TIME = 0.3
    LONG_SLEEP_TIME = 3
    SOLUTION_COUNT = 1
    GROUP_ONE, GROUP_TWO, GROUP_THREE = 0, 1, 2

    def __init__(self):
        self.current_group = None

    def process_solution(self):

        try:
            entry = Webscraper()
            entry.navigate_to_url(PageElements.base_url)
        except Exception as pageError:
            return f'An error occurred on URL navigation: {pageError}'

        # Contain dynamic variable for possible gold options
        num_gold_bars = entry.scrape_gold_elements()
        self.current_group = list(range(0,num_gold_bars))

        # # Loop through the current group and split into 3
        while (len(self.current_group)) > self.SOLUTION_COUNT:
            half_length = len(self.current_group) // 2
            grouped_array = [self.current_group[i:i+half_length] for i in range(0,len(self.current_group),half_length)]

            # Weigh the gold
            for index, (left_gold, right_gold) in enumerate(zip(grouped_array[0],grouped_array[1])):
                entry.left_basket(left_gold, index)
                entry.right_basket(right_gold, index)
                time.sleep(self.SHORT_SLEEP_TIME)

            entry.click_weigh()
            weigh_results = entry.get_weigh_results()
            WebDriverWait(entry.driver, self.LONG_SLEEP_TIME).until(
                lambda driver: driver.find_element(By.XPATH, PageElements.results_xpath).text != PageElements.results_reset_text
            )

            # Check the weighed results
            for operator in weigh_results:
                if "=" in operator:
                    self.current_group = grouped_array[self.GROUP_THREE]
                    break
                elif "<" in operator:
                    self.current_group = grouped_array[self.GROUP_ONE]
                    break
                else:
                    self.current_group = grouped_array[self.GROUP_TWO]
            entry.click_reset()

        # Select and validate the fake gold is found
        for selection in self.current_group:
            entry.select_fake_bar(selection)
            alert = Alert(entry.driver)
            alert_text = alert.text

            try:
                if alert_text == PageElements.correct_alert_text:
                    print(f'Fake gold determined: {selection}')
                    break
                else:
                    print('Test failed to find the fake gold')
                    break

            except NoAlertPresentException:
                print('No alert found')

        time.sleep(self.LONG_SLEEP_TIME)
        alert.dismiss()
        entry.close_browser()

if __name__ == "__main__":
    solution_instance = Main()
    solution_instance.process_solution()