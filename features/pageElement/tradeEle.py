from selenium.webdriver.common.by import By

class TradeEle:
    pair_toggle = (By.XPATH, '//div[@class="pair-toggle"]')
    last_price_title = (By.XPATH, '//div[@class="item-title" and text()="Last Price"]')
    high_price_title = (By.XPATH, '//div[@class="item-title" and text()="High"]')
    low_price_title = (By.XPATH, '//div[@class="item-title" and text()="Low"]')