from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from pip._internal.utils.misc import display_path
import pyautogui


chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(15)

driver.get("https://qado.medisource.com")
driver.maximize_window()

usernametb = driver.find_element_by_id('loginemail').send_keys('superagent@geeksnest')
time.sleep(3)

passwordtb = driver.find_element_by_id('loginpassword').send_keys('Tester2021@')
time.sleep(3)

loginbtn = driver.find_element_by_xpath('/html/body/section/div/div[2]/form/div[6]/button')
loginbtn.click()
time.sleep(5)

driver.get("https://qado.medisource.com/library/blank-forms")
driver.maximize_window()
time.sleep(5)
Editbtn = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button').click()
time.sleep(3)


uploadbtn = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[1]').click()
time.sleep(5)

browsebtn = driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div/div[2]/div/div/button').click()
time.sleep(5)
pyautogui.click(347,386)
time.sleep(5)
pyautogui.click(486,308)
time.sleep(5)
pyautogui.click(781,582)
time.sleep(5)
















# browsebtn = driver.find_element_by_xpath('/html/body/div[12]/div/div/div/div/div[2]/div/div/button').click()
# image_path=os.path.abspath('C:/Users/HP/Pictures/Borders/border.jpg')
# driver.find_element_by_id("/html/body/div[12]/div/div/div/div/div[2]/div/div/button").send_keys(image_path)  
#("C:\\Users\\HP\\Pictures\\Borders\\border.jpg")
#driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/div[2]/div/div/button').click()

# browsebtn = driver.find_element_by_xpath("/html/body/div[12]/div/div/div/div/div[2]/div/div/button").click()
# upload.get_attribute('C:\\Users\\HP\\Pictures\\Borders\\border.jpg').send_keys()   
# imageget = get_attribute("C:/Users/HP/Pictures/Borders/border.jpg").click()

#browseimage = driver.driver.find_element_by_xpath("/html/body/div[12]/div/div/div/div/div[2]/div/div/button").click()
#send_keys(os.getcwd()+"C:\\Users\\HP\\Pictures\\Borders\\border.jpg")


#driver.find_element_by_xpath('/html/body/div[11]/div/div/div/div/div[2]/div/div/button').get_attribute('value')
#time.sleep(5)






 







