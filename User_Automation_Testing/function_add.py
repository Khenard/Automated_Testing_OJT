from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def user_add():

    fname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[1]/td[2]/div/input')
    fname.send_keys('Cat')
    time.sleep(2)
    
    lname = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[2]/td[2]/div/input')
    lname.send_keys('RN')
    time.sleep(2)
    
    minitial = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[3]/td[2]/div/input')
    minitial.send_keys('M.')
    time.sleep(2)
    
    suffixtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[4]/td[2]/div/input')
    suffixtb.send_keys('II')
    time.sleep(2)
    
    gendertb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[5]/td[2]/div/ng-form/label[2]/input')
    gendertb.click()
    time.sleep(2)
    
    bdate = config.driver.find_element_by_xpath('//*[@id="birthdate"]')
    bdate.send_keys('08091990')
    time.sleep(2)
    
    racetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a')
    racetb.click()
    time.sleep(2)
    
    selectRace = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a/span')
    selectRace.click()
    time.sleep(2)
    
    maritalStats = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    maritalStats.send_keys('96799')
    time.sleep(2)
    
    disciplinetb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    disciplinetb.send_keys('96799')
    time.sleep(2)
    
    titletb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    titletb.send_keys('96799')
    time.sleep(2)
    
    hireCat = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    hireCat.send_keys('96799')
    time.sleep(2)
    
    positiontb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    positiontb.send_keys('96799')
    time.sleep(2)
    
    ssstb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    ssstb.send_keys('96799')
    time.sleep(2)
    
    cliniciantb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    cliniciantb.send_keys('96799')
    time.sleep(2)
    
    companytb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    companytb.send_keys('96799')
    time.sleep(2)
    
    address1 = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    address1.send_keys('96799')
    time.sleep(2)
    
    address2 = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    address2.send_keys('96799')
    time.sleep(2)

    citytb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    citytb.send_keys('96799')
    time.sleep(2)
    
    statetb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    statetb.send_keys('96799')
    time.sleep(2)
    
    zipCode = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    zipCode.send_keys('96799')
    time.sleep(2)
    
    phoneNo = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    phoneNo.send_keys('96799')
    time.sleep(2)
    
    mobileNo = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    mobileNo.send_keys('96799')
    time.sleep(2)
    
    faxtb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    faxtb.send_keys('96799')
    time.sleep(2)
    
    emailtb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    emailtb.send_keys('96799')
    time.sleep(2)
    
    hireDate = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    hireDate.send_keys('96799')
    time.sleep(2)
    
    terminationDate = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    terminationDate.send_keys('96799')
    time.sleep(2)
    
    primaryLang = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryLang.send_keys('96799')
    time.sleep(2)
    
    secondaryLang = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryLang.send_keys('96799')
    time.sleep(2)
    
    otherLang = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherLang.send_keys('96799')
    time.sleep(2)
    
    primaryVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryVerbal.send_keys('96799')
    time.sleep(2)
    
    secondaryVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryVerbal.send_keys('96799')
    time.sleep(2)
    
    otherVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherVerbal.send_keys('96799')
    time.sleep(2)
    
    primaryReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryReading.send_keys('96799')
    time.sleep(2)
    
    secondaryReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryReading.send_keys('96799')
    time.sleep(2)
    
    otherReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherReading.send_keys('96799')
    time.sleep(2)
    
    primaryWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryWriting.send_keys('96799')
    time.sleep(2)
    
    secondaryWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryWriting.send_keys('96799')
    time.sleep(2)
    
    otherWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherWriting.send_keys('96799')
    time.sleep(2)
    
    


     
   
    
    
    
    
    
    
    
    