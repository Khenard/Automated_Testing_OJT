from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import function
import config


config.driver.get("https://qado.medisource.com/login")
config.driver.maximize_window()

function.loginfunction('superagent@unitest', 'Tester2021@')

time.sleep(5)

config.driver.get('https://qado.medisource.com/patients/admitted')
time.sleep(3)



def searchpatient():
    searchtb = config.driver.find_element_by_css_selector('#searchbar__wrapper > div > input').send_keys('automated')


searchpatient()





