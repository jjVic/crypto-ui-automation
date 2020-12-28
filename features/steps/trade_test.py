from behave import *
import traceback

from features.UTIL import utils
from features.pageObject.exchangePO import ExchangePageObject
from features.pageObject.tradePO import TradePageObject


@given("I am on Cypto Exchange page")
def step_impl(context):
    try:
        context.exchange_page = ExchangePageObject(context.webdriver)
        context.exchange_page.handle_cookie_alert()
    except Exception as e:
        traceback.print_exc()
        utils.screenshot(context.webdriver, context.scenario.name)
        raise(e)


@step('I choose my markets "{markets}"')
def step_impl(context, markets):
    try:
        context.selected_markets = markets
        context.exchange_page.select_market(context.selected_markets)
    except Exception as e:
        traceback.print_exc()
        utils.screenshot(context.webdriver, context.scenario.name)
        raise (e)


@when('I click trade for a coin pair "{coin_pair}"')
def step_impl(context, coin_pair):
    try:
        context.trade_page = TradePageObject(context.webdriver)
        context.exchange_page.click_trade_button_for_coin_pair(context.selected_markets, coin_pair)
        context.is_on_coin_trade_page = context.trade_page.is_on_trade_Page()
        assert context.is_on_coin_trade_page
        context.is_navigated_to_coin_pair_trade_page = context.trade_page.is_navigated_to_selected_coin_pair_trade_page(coin_pair)
    except Exception as e:
        traceback.print_exc()
        utils.screenshot(context.webdriver, context.scenario.name)
        raise(e)


@then("I should see the coin pair trade page")
def step_impl(context):
    try:
        assert context.is_navigated_to_coin_pair_trade_page
    except Exception as e:
        traceback.print_exc()
        utils.screenshot(context.webdriver, context.scenario.name)
        raise(e)


