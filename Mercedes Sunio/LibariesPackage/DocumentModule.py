from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import pyautogui


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

driver.get("https://qado.medisource.com/library/documents")
time.sleep(5)
Editbtn = driver.find_element_by_xpath('/html/body/section/section/data/ui-view/div[1]/div/div/div/div/div/div/button').click()
time.sleep(3)

uploadbtn = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[1]').click()
time.sleep(5)


browsebtn = driver.find_element_by_css_selector('body > div.modal.fade.ng-isolate-scope.patient-records-upload.in > div > div > div > div > div.container > div > div > button').click()
time.sleep(5)

pyautogui.click(333,386)
time.sleep(5)
pyautogui.click(611,301)
time.sleep(5)
pyautogui.click(772,580)
time.sleep(5)





 







