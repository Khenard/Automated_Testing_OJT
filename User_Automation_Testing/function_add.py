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
    
    genderCb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[5]/td[2]/div/ng-form/label[2]/input')
    genderCb.click()
    time.sleep(2)
    
    bdate = config.driver.find_element_by_xpath('//*[@id="birthdate"]')
    bdate.send_keys('08091990')
    time.sleep(2)
    
    raceDdown = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/a')
    raceDdown.click()
    time.sleep(2)
    
    selectRace = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[7]/td[2]/div/div/div/div')
    selectRace.click()
    time.sleep(2)
    
    maritalStats = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/a')
    maritalStats.click()
    time.sleep(2)
    
    selectMarital = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[8]/td[2]/div/div/div/div')
    selectMarital.click()
    time.sleep(2)
    
    disciplinetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/a')
    disciplinetb.click()
    time.sleep(2)
    
    selectDiscipline = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[9]/td[2]/div/div/div/div')
    selectDiscipline.click()
    time.sleep(2)
    
    titletb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/a')
    titletb.click()
    time.sleep(2)
    
    selectTitle = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[10]/td[2]/div/div/div/div')
    selectTitle.click()
    time.sleep(2)
    
    hireCat = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/a')
    hireCat.click()
    time.sleep(2)
    
    selectHireCat = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[11]/td[2]/div/div/div/div')
    selectHireCat.click()
    time.sleep(2)
    
    positiontb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/a')
    positiontb.click()
    time.sleep(2)
    
    selectPosition = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[12]/td[2]/div/div/div/div')
    selectPosition.click()
    time.sleep(2)
    
    ssstb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[13]/td[2]/div/input')
    ssstb.send_keys('1225566998')
    time.sleep(2)
    
    cliniciantb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[14]/td[2]/div/input')
    cliniciantb.send_keys('236899978')
    time.sleep(2)
    
    companytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[15]/td[2]/div/input')
    companytb.send_keys('Winterfell Company')
    time.sleep(2)
    
    address1 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[16]/td[2]/div/textarea')
    address1.send_keys('2411 Tycos Dr')
    time.sleep(2)
    
    address2 = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[17]/td[2]/div/textarea')
    address2.send_keys('2556 Tycose Dr')
    time.sleep(2)

    citytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[18]/td[2]/div/input')
    citytb.send_keys('Toronto')
    time.sleep(2)
    
    statetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[19]/td[2]/div/div/div/a')
    statetb.click()
    time.sleep(2)
    
    #selectState = config.driver.find_elements_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[19]/td[2]/div/div/div/a/div')
    #selectState.click()
    #time.sleep(2)
    
    zipCode = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[20]/td[2]/div/input')
    zipCode.send_keys('91001')
    time.sleep(2)
    
    phoneNo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[21]/td[2]/div/input')
    phoneNo.send_keys('2013336666')
    time.sleep(2)
    
    mobileNo = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[22]/td[2]/div/input')
    mobileNo.send_keys('2015558888')
    time.sleep(2)
    
    faxtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[23]/td[2]/div/input')
    faxtb.send_keys('2017778888')
    time.sleep(2)
    
    emailtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[1]/tbody/tr[24]/td[2]/div/input')
    emailtb.send_keys('catrn@mailinator.com')
    time.sleep(2)
    
    hireDate = config.driver.find_element_by_xpath('//*[@id="hireddate"]')
    hireDate.send_keys('06102021')
    time.sleep(2)
    
    terminationDate = config.driver.find_element_by_xpath('//*[@id="terminationdate"]')
    terminationDate.send_keys('06102030')
    time.sleep(2)
    
    primaryLang = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[3]/tbody/tr[1]/td[2]/div/div/div/a')
    primaryLang.click()
    time.sleep(2)
    
    selectPrimaryLang = config.driver.find_elements_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[3]/tbody/tr[1]/td[2]/div/div/div/div')
    selectPrimaryLang.click()
    time.sleep(2)
    
    secondaryLang = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[3]/tbody/tr[1]/td[3]/div/div/div/div')
    secondaryLang.click()
    time.sleep(2)
    
    selectsecondaryLang = config.driver.find_elements_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/fieldset/table[3]/tbody/tr[1]/td[2]/div/div/div/div')
    selectsecondaryLang.click()
    time.sleep(2)
    
    otherLang = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherLang.click()
    time.sleep(2)
    
    primaryVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryVerbal.click()
    time.sleep(2)
    
    secondaryVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryVerbal.click()
    time.sleep(2)
    
    otherVerbal = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherVerbal.click()
    time.sleep(2)
    
    primaryReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryReading.click()
    time.sleep(2)
    
    secondaryReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryReading.click()
    time.sleep(2)
    
    otherReading = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherReading.click()
    time.sleep(2)
    
    primaryWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    primaryWriting.click()
    time.sleep(2)
    
    secondaryWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    secondaryWriting.click()
    time.sleep(2)
    
    otherWriting = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    otherWriting.click()
    time.sleep(2)
    
    


     
   
    
    
    
    
    
    
    
    