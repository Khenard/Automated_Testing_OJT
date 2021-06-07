from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import function_login
import config
import function_add
import function_edit


config.driver.get("https://qado.medisource.com/login")
config.driver.maximize_window()

time.sleep(3)

function_login.loginfunction('superagent@geeksnest','Tester2021@')


time.sleep(10)

config.driver.get("https://qado.medisource.com/hospital")
config.driver.maximize_window()

time.sleep(5)

function_add.hospital_facility_add()

time.sleep(5)

config.driver.get("https://qado.medisource.com/hospital")

time.sleep(5)

function_edit.hospital_facility_edit()

time.sleep(5)





















