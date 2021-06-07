from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config

 
def loginfunction(un, pw):

    usernametb = config.driver.find_element_by_name('loginemail').send_keys(un)
    time.sleep(3)

    passwordtb = config.driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(pw)
    time.sleep(3)

    loginbtn = config.driver.find_element_by_xpath('//*[@id="mhLP-ln"]/div[2]/form/div[6]/button').click()
    
    
    
    
    
