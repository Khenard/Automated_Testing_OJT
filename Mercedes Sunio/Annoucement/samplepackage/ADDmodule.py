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
announcebtn = driver.find_element_by_xpath('/html/body/section/section/data/div/div[1]/div/div/a').click()

namecontent = driver.find_element_by_xpath('/html/body/section/section/data/div/div[2]/form/table/tbody/tr/td/div[1]/div[3]/textarea').send_keys('MEETING! on May 28, 2021 @ Gymnasium. 1:00 pm')
time.sleep(5)

date = driver.find_element_by_xpath('/html/body/section/section/data/div/div[2]/form/table/tbody/tr/td/div[1]/div[2]/table/tbody/tr/td[4]/div/input')
date.send_keys('06/02/2021')
time.sleep(5)

postbtn = driver.find_element_by_xpath('/html/body/section/section/data/div/div[2]/form/table/tbody/tr/td/div[2]/a').click()
time.sleep(5)

showbtn = driver.find_element_by_xpath('/html/body/section/section/data/div/div[1]/div/div/a').click()
time.sleep(5)







