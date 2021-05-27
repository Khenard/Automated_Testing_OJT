from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
# from datetime import datetime


chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get("https://qado.medisource.com/login")
driver.maximize_window()

time.sleep(3)

qausername = driver.find_element_by_xpath('//*[@id="loginemail"]').send_keys('superagent@geeksnest')
time.sleep(3)

qapassword = driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys('Tester2021@')
time.sleep(3)

qalogin = driver.find_element_by_xpath('/html/body/section/div/div[2]/form/div[6]/button').click()
time.sleep(3)


# redirecting to joint chha visit
driver.get("https://qado.medisource.com/patientcare/153F11C0-54B1-45DE-8FA2-13601A5BA95C/702DD393-A2A7-4B95-B960-117F108472A2/sv/notes/D2CD8BB3-0FFA-4E06-AFBA-40EF9C61E22A/CHHA/8218FA77-8BB4-475B-96C4-D7EA5534D2CB")
time.sleep(3)


clinician = driver.find_element_by_xpath('/html/body/section/section/data/section/div[2]/div/div/div/div/div/div/form/div[1]/fieldset/div/table[1]/tbody/tr/td[2]/table/tbody/tr/td/label[1]/input').click()
visitdate = driver.find_element_by_xpath('//*[@id="visitDate"]').clear()
# visitdate = datetime.datetime(now)
visitdate1 = driver.find_element_by_xpath('//*[@id="visitDate"]').send_keys('06082021')
time.sleep(3)

chhadd = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/div').click()
chhadd2 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/div/div/ul/li').click()
time.sleep(3)

met1 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/label/input').click()
met2 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[4]/td[1]/label/input').click()
met3 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[5]/td[1]/label/input').click()
met4 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[6]/td[1]/label/input').click()
met5 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[7]/td[1]/label/input').click()
met6 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[8]/td[1]/label/input').click()
met7 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[9]/td[1]/label/input').click()
met8 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[10]/td[1]/label/input').click()
met9 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[11]/td[1]/label/input').click()
met10 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[12]/td[1]/label/input').click()
met11 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[13]/td[1]/label/input').click()
met12 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[14]/td[1]/label/input').click()
met13 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[15]/td[1]/label/input').click()
me14 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[16]/td[1]/label/input').click()
met15 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[2]/td/table/tbody/tr[17]/td[1]/label/input').click()
time.sleep(3)

comment1 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[4]/td/table/tbody/tr/td/div/div/textarea').click()
comment1 = driver.find_element_by_xpath('//*[@id="parent"]/div/div/form/div[1]/fieldset/div/table[3]/tbody/tr[4]/td/table/tbody/tr/td/div/div/textarea').send_keys('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum')