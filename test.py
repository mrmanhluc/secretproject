from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
# import os, time, datetime, re, util, sys
import selenium.webdriver.chrome.service as service
import platform

class Sample():
    def __init__(self):
        os_name = platform.system()
        driver_address = 'chromedriver.exe' if os_name == 'Windows' else '/usr/local/bin/chromedriver'
        self.aservice = service.Service(driver_address)
        self.aservice.start()
        capabilities = {'chrome.binary': '/usr/bin/google-chrome-stable', "chromeOptions": {"args": ['--no-sandbox']}}
        self.driver = webdriver.Remote(self.aservice.service_url, capabilities)
        self.driver.implicitly_wait(3)
        self.base_url = "https://vnexpress.net"

    def __del__(self):
        self.driver.close()

    def sample(self):
        driver = self.driver

        try:
            driver.get(self.base_url)
            result = driver.find_element_by_id("myvne_taskbar")
            print(result.text)
        except:
            print("Error")
        finally:
            print("done")

sample = Sample()
sample.sample()