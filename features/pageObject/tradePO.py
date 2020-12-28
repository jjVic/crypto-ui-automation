from features.UTIL.webBasePageObject import WebPageObject
from features.pageElement.tradeEle import TradeEle
from features.UTIL import utils
from features.UTIL import general

class TradePageObject(WebPageObject):
    def is_on_trade_Page(self):
        try:
            self.find_element(TradeEle.last_price_title, timeout=general.page_load_timeout)
            self.find_element(TradeEle.high_price_title)
            self.find_element(TradeEle.low_price_title)
            return True
        except:
            return False

    def is_navigated_to_selected_coin_pair_trade_page(self, coin_pair):
        utils.log('selected coin pair:' + coin_pair)
        is_navigated = False
        coin_pair_toggle_text = self.get_text_from_element(TradeEle.pair_toggle)
        utils.log('coin pair toggle text :' +  coin_pair_toggle_text)
        if coin_pair in coin_pair_toggle_text:
            is_navigated = True
        return is_navigated