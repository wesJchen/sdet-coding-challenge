import time
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

    def __init__(self):
        self.current_group = None

    def process_solution(self):
        entry = Webscraper()
        entry.navigate_to_url(PageElements.base_url)

        # Contain dynamic variable for possible gold options
        num_gold_bars = entry.scrape_gold_elements()
        self.current_group = list(range(0,num_gold_bars))

        # Loop through current group (total gold options to check) after splitting into three subgroups
        while (len(self.current_group)) > self.SOLUTION_COUNT:
            half_length = len(self.current_group) // 2
            grouped_array = [self.current_group[i:i+half_length] for i in range(0,len(self.current_group),half_length)]

            # Weigh the first and second subgroups
            for index, (left_gold, right_gold) in enumerate(zip(grouped_array[0],grouped_array[1])):
                entry.left_basket(left_gold, index)
                entry.right_basket(right_gold, index)
                time.sleep(self.SHORT_SLEEP_TIME)

            entry.click_weigh()
            WebDriverWait(entry.driver, self.LONG_SLEEP_TIME).until(Webscraper.weigh_results_update)
            weigh_results = entry.get_weigh_results()

            # Check the weighed results (Assume [0]: Group one, [1]: Group two, [2]: Group three)
            for operator in weigh_results:
                if "=" in operator:
                    self.current_group = grouped_array[2]
                    break
                elif "<" in operator:
                    self.current_group = grouped_array[0]
                    break
                else:
                    self.current_group = grouped_array[1]
            entry.click_reset()

        # Select and validate the fake gold is found
        for selection in self.current_group:
            entry.click_fake_bar(selection)
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