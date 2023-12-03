from selenium.webdriver.common.by import By

class PageElements:

    base_url = "http://sdetchallenge.fetch.com/"

    reset_button_xpath = '/html/body/div/div/div[1]/div[4]/button[1]'    
    weigh_button_xpath = '//*[@id="weigh"]'

    gold_options = '//*[@id="root"]/div/div[2]'

    results_xpath = '//*[@id="root"]/div/div[1]/div[5]/ol'