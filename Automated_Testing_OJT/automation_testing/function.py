from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def loginfunction(un, up):
    
    time.sleep(5)
    usernametb = config.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/form/div[1]/input').send_keys(un)
    time.sleep(5)
    passwordtb = config.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/form/div[2]/input')
    passwordtb.send_keys(up)
    time.sleep(3)
    loginbtn = config.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div/div/form/div[3]/div[1]/button')
    loginbtn.click() 