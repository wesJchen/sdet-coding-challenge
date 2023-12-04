import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

from page_objects.elements import PageElements
from src.page_methods.browser_methods import Webscraper

class Main:
    def __init__(self):
        self.current_group = None

    def process_solution(self):
        short_sleep_time = 0.3
        long_sleep_time = 3

        try:
            entry = Webscraper()
            entry.navigate_to_url(PageElements.base_url)
        except Exception as pageError:
            return f'An error occurred on URL navigation: {pageError}'

        # Contain a variable of all possible gold options
        num_gold_bars = entry.scrape_gold_elements()
        self.current_group = list(range(0,num_gold_bars))

        # # Loop through the current group and split into 3
        while (len(self.current_group)) > 1:
            half_length = len(self.current_group) // 2
            grouped_array = [self.current_group[i:i+half_length] for i in range(0,len(self.current_group),half_length)]

            # Weigh the gold bars
            for index, (left_gold, right_gold) in enumerate(zip(grouped_array[0],grouped_array[1])):
                entry.left_basket(str(left_gold),index)
                entry.right_basket(str(right_gold),index)
                time.sleep(short_sleep_time)

            entry.click_weigh()
            results = entry.get_weigh_results()
            WebDriverWait(entry.driver, long_sleep_time).until(
                lambda driver: driver.find_element(By.XPATH, PageElements.results_xpath).text != PageElements.results_reset_text
            )

            # Check the weighed bars
            for check in results:
                if "=" in check:
                    self.current_group = grouped_array[2]
                    break
                elif "<" in check:
                    self.current_group = grouped_array[0]
                else:
                    self.current_group = grouped_array[1]
            entry.click_reset()

        # Select the correct fake bar
        for x in self.current_group:
            entry.select_fake_bar(str(x))
            alert = Alert(entry.driver)
            alert_text = alert.text

            try:
                if alert_text == PageElements.correct_alert_text:
                    print(f'The fake gold is in option {x}')
                    break
                else:
                    print('Test failed to find the fake gold')
                    break

            except NoAlertPresentException:
                print('No alert found')

        time.sleep(long_sleep_time)
        alert.dismiss()
        entry.close_browser()

if __name__ == "__main__":
    solution_instance = Main()
    solution_instance.process_solution()