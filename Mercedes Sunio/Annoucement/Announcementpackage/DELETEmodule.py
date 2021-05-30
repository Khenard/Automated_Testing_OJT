from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get("https://qado.medisource.com")
driver.maximize_window()

usernametb = driver.find_element_by_id('loginemail').send_keys('superagent@geeksnest')
time.sleep(3)

passwordtb = driver.find_element_by_id('loginpassword').send_keys('Tester2021@')
time.sleep(3)

loginbtn = driver.find_element_by_xpath('/html/body/section/div/div[2]/form/div[6]/button')
loginbtn.click()

time.sleep(5)

driver.get("https://qado.medisource.com/announcements/manage")
time.sleep(5)

deletebtn = driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/table/tbody/tr[2]/td[2]/div/a[1]')
deletebtn.click()
time.sleep(3)

yesbtn =  driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]')
yesbtn.click()


