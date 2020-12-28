from features.UTIL import general
from features.UTIL import utils
import time
from selenium.webdriver.common.by import By

import traceback
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebPageObject(object):
    def __init__(self, driver):
        self.webdriver = driver

    def find_element(self, locator, timeout=general.default_timeout, is_visible=True):
        try:
           if is_visible:
               element = WebDriverWait(self.webdriver, timeout).until(EC.visibility_of_element_located(locator))
               return element
           else:
               element = WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located(locator))
               return element
        except Exception as e:
            traceback.print_exc()
            utils.log(locator[1] + " not found")
            raise e

    def find_elements(self, locator, timeout=general.default_timeout, is_visible=True):
        try:
           if is_visible:
               elements = WebDriverWait(self.webdriver, timeout).until(EC.visibility_of_all_elements_located(locator))
               return elements
           else:
               elements = WebDriverWait(self.webdriver, timeout).until(EC.presence_of_all_elements_located(locator))
               return elements
        except Exception as e:
            traceback.print_exc()
            utils.log(locator[1] + " not found")
            raise e

    def click_element(self, locator, timeout=general.default_timeout):
        try:
            element = WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located(locator))
            element.click()
        except:
            try:
                element = WebDriverWait(self.webdriver, timeout).until(EC.element_to_be_clickable(locator))
                element.click()
            except:
                try:
                    element = WebDriverWait(self.webdriver, timeout).until(EC.visibility_of_element_located(locator))
                    self.webdriver.execute_script("arguments[0].click();", element)
                except Exception as e:
                    traceback.print_exc()
                    utils.log(locator[1] + " cannot be clicked")

    def click_by_Xpath(self, xpath, timeout=general.default_timeout):
        try:
            element = WebDriverWait(self.webdriver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.click()
        except Exception:
            traceback.print_exc()
            utils.log(xpath + " cannot be clicked")

    def find_by_Xpath(self, xpath, timeout=general.default_timeout):
        try:
            element = WebDriverWait(self.webdriver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception:
            traceback.print_exc()
            utils.log(xpath + " not found")

    def get_text_from_element(self, locator, timeout=general.default_timeout):
        try:
            element = self.find_element(locator, timeout)
            element_text = element.text
            return element_text
        except Exception as e:
            utils.log("Fail to find text for " + locator[1])
            raise e

    def screenshot(self, name):
        screendir = utils.check_screen_shot_report_folder()
        try:
            timestamp = str(time.strftime("%Y%m%d-%H%M%S"))
            screenshot_name = timestamp + "_" + name + ".png"
            utils.log("Taking screenshot:" + screendir + screenshot_name)
            self.webdriver.get_screenshot_as_file(screendir + screenshot_name)
        except Exception as e:
            print(e)