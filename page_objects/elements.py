class PageElements:
    base_url = "http://sdetchallenge.fetch.com/"

    # Buttons
    reset_button_xpath = '/html/body/div/div/div[1]/div[4]/button[1]'    
    weigh_button_xpath = '//*[@id="weigh"]'

    # Gold options
    gold_options_xpath = '//*[@id="root"]/div/div[2]'
    gold_options_child_xpath = './*'

    # Basket locators
    left_basket_id = 'left_{}'
    right_basket_id = 'right_{}'

    # Solution Locators
    results_xpath = '//*[@id="reset"]'
    results_reset_text = '?'

    fake_bar_solution_xpath = '//*[@id="coin_{}"]'
    incorrect_alert_text ='Oops! Try Again!' 
    correct_alert_text = 'Yay! You find it!'