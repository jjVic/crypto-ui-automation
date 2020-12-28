from behave import fixture, use_fixture

from features.UTIL.driverConfig import Configuration

@fixture
def setup_browser(context):
    # -- SETUP-FITURE PART:
    setup = Configuration()
    context.webdriver = setup.get_chrome_driver()
    yield context.webdriver
    # -- CLEANUP-FIXTURE PART:
    context.webdriver.quit()

def before_scenario(context, scenario):
    use_fixture(setup_browser, context)
