import os
import sys

from selenium import webdriver

project_folder = os.path.normpath(sys.path[0])

from features.UTIL import utils


class Configuration:
    def __init__(self):
        utils.log("PROJECT PATH: "+project_folder)
        self.chromeDriverPath = project_folder + '/features/UTIL/driver/chromedriver.exe'
        self.testEnvironment = "https://crypto.com/exchange"

    def get_chrome_driver(self):
        driver = webdriver.Chrome(executable_path=self.chromeDriverPath)
        driver.get(self.testEnvironment)
        driver.maximize_window()
        return driver
