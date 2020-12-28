import os
import sys
import time

project_folder = os.path.normpath(sys.path[0])

today = time.strftime("%Y%m%d")

def log(msg):
    try:
        print(f'{time.strftime("%H:%M:%S")} : {msg}')
    except Exception as e:
        print(e)

def check_screen_shot_report_folder():
    log("project_folder:"+project_folder)
    reportPath = project_folder + "features/screenshot_report/" + today
    if not os.path.exists(reportPath):
        os.makedirs(reportPath)
    return reportPath + "/"

def screenshot(driver, name):
    screendir = check_screen_shot_report_folder()
    try:
        timestamp = str(time.strftime("%Y%m%d-%H%M%S"))
        screenshot_name = timestamp + "_" + name + ".png"
        log("Taking screenshot:" + screendir +screenshot_name)
        driver.get_screenshot_as_file(screendir + screenshot_name)
    except Exception as e:
        print(e)
