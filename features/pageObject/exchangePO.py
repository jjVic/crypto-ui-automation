from features.UTIL.webBasePageObject import WebPageObject
from features.pageElement.exchangeEle import ExchangeEle
from selenium.webdriver.common.keys import Keys

from features.UTIL import utils
from features.UTIL import general


class ExchangePageObject(WebPageObject):
    def is_on_exchange_page(self):
        try:
            self.find_element(ExchangeEle.exchange_title, timeout=general.page_load_timeout)
            return True
        except:
            return False

    def handle_cookie_alert(self):
        try:
            self.find_element(ExchangeEle.alert_box, timeout=general.page_load_timeout)
            self.click_element(ExchangeEle.accept_cookie_button)
        except:
            pass

    def select_market(self, market):
        utils.log("SELECTED MARKET:" + str(market))
        markets = self.find_elements(ExchangeEle.market_tabs)
        for mrkt in markets:
            if mrkt.text == market:
                mrkt.click()

    def click_trade_button_for_coin_pair(self, market, coin_pair):
        utils.log("SELECTED COIN PAIR:" + coin_pair)
        source = coin_pair.split('/')[0]
        target = coin_pair.split('/')[1]
        target_formatted = "/" + coin_pair.split('/')[1]

        if str(market) == "BTC Markets":
            selected_market = "BTC"
        elif str(market) == "USDT Markets":
            selected_market = "USDT"
        elif str(market) == "CRO Markets":
            selected_market = "CRO"

        utils.log("source:" + source)
        utils.log("target:" + target)
        utils.log("selected market:" + selected_market)

        if source == selected_market and target != selected_market:   # For ex: CRO/USDC
            coin_pair_trade_button_xpath = ExchangeEle.coin_pair_trade_button_from_target[1].replace('replace_value', target_formatted)
        elif target == selected_market and source != selected_market:  # For ex: ZIL/CRO
            coin_pair_trade_button_xpath = ExchangeEle.coin_pair_trade_button_from_source[1].replace('replace_value', source)

        trade_elem = self.find_by_Xpath(coin_pair_trade_button_xpath)
        trade_elem.send_keys(Keys.ENTER)







