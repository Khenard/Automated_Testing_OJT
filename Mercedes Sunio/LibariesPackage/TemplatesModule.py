from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains



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

driver.get("https://qado.medisource.com/narratives/templates")
time.sleep(5)

searchbtn = driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys('Automate')
time.sleep(5)

dropbtn = driver.find_element_by_css_selector('#content > data > div.container.ng-scope > ui-view > div > div.advanced__search_container.clearfix > div > div:nth-child(2) > div > div > div')
dropbtn.click()
time.sleep(5)

inputbtn = driver.find_element_by_css_selector('#content > data > div.container.ng-scope > ui-view > div > div.advanced__search_container.clearfix > div > div:nth-child(2) > div > div > div > div > div > input[type=text]')
time.sleep(3)
action = ActionChains(driver)
action.move_to_element(inputbtn).send_keys("Special Procedures")
action.perform()
#inputbtn.send_keys('Special Procedures').perform()

#time.sleep(3)
#inputbtn.enter()


#Newbtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[1]/a').click()
#time.sleep(3)











 







