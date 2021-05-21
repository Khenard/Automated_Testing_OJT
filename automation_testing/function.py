from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def loginfunction(un, up):
    
    time.sleep(5)
    usernametb = config.driver.find_element_by_id('loginemail').send_keys(un)
    time.sleep(5)
    passwordtb = config.driver.find_element_by_id('loginpassword')
    passwordtb.send_keys(up)
    time.sleep(3)
    loginbtn = config.driver.find_element_by_xpath('//*[@id="mhLP-ln"]/div[2]/form/div[6]/button')
    loginbtn.click() 