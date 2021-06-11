from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config



def user_edit():
    
    editbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[3]/td[7]/div/button[1]')
    editbtn.click()
    time.sleep(10)
    
    fname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[1]/td[2]/div/input')
    fname.clear()
    fname.send_keys('')
    time.sleep(2)
    
    lname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[2]/td[2]/div/input')
    lname.clear()
    lname.send_keys('')
    time.sleep(2)
    
    minitial = config.driver.find_element_by_xpath('')
    minitial.clear()
    minitial.send_keys('')
    time.sleep(2)
    
    suffixtb = config.driver.find_element_by_xpath('')
    suffixtb.clear()
    suffixtb.send_keys('')
    time.sleep(2)
    
    genderCb = config.driver.find_element_by_xpath('')
    genderCb.click()
    time.sleep(2)
    
    bdate = config.driver.find_element_by_xpath('')
    bdate.clear()
    bdate.send_keys('')
    time.sleep(2)
    
    raceDdown = config.driver.find_element_by_xpath('')
    raceDdown.click()
    time.sleep(2)
    
    
    
