from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import function_login
import config
import function_addPhysician
import function_editPhysician



config.driver.get("https://qado.medisource.com/login")
config.driver.maximize_window()

time.sleep(3)

function_login.loginfunction('superagent@geeksnest','Tester2021@')


time.sleep(10)

config.driver.get("https://qado.medisource.com/physicians")
config.driver.maximize_window()

time.sleep(10)

function_addPhysician.physician_add()

time.sleep(10)

config.driver.get("https://qado.medisource.com/physicians")

time.sleep(5)

function_editPhysician.physician_edit()























