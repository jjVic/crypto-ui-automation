from selenium.webdriver.common.by import By

class ExchangeEle:
    exchange_title = (By.XPATH, '//h1[text()="Crypto.com Exchange"]')
    market_tabs = (By.XPATH, '//div[contains(@class,"e-tabs__nav-item")]')
    coin_pair_trade_button_from_source = (By.XPATH, '//span[@class="source" and text()="replace_value"] /../../..//button[contains(@class, "trade-btn")]')
    coin_pair_trade_button_from_target = (By.XPATH, '//span[@class="target" and text()="replace_value"] /../../..//button[contains(@class, "trade-btn")]')

    alert_box = (By.XPATH, '//div[@class="optanon-alert-box-wrapper  "]')
    accept_cookie_button = (By.XPATH, '//button[@class="optanon-allow-all accept-cookies-button"]')




