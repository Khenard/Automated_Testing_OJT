from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time


chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get("https://app2.woundtrack.com/login")
driver.maximize_window()

time.sleep(3)

usernametb = driver.find_element_by_name('loginemail').send_keys('woundtrackdemo')
time.sleep(3)

passwordtb = driver.find_element_by_name('loginpassword').send_keys('Woundtrack2020@')
time.sleep(3)

loginbtn = driver.find_element_by_xpath('//*[@id="mCSB_1_container"]/div[2]/form/button').click()












