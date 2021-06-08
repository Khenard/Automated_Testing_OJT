from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config



def physician_add():

    newbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a')
    newbtn.click()
    time.sleep(5)
    
    skipbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/div/div[1]/button[1]')
    skipbtn.click()
    time.sleep(5)
    
    #stateDrop = config.driver.find_element_by_xpath('//*[@id="state"]')
    #stateDrop.click()
    #time.sleep(5)
    
    fnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/div/input')
    fnametb.send_keys('Sansa')
    time.sleep(2)
    
    mnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/div/input')
    mnametb.send_keys('Gambys')
    time.sleep(2)
    
    lnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/div/input')
    lnametb.send_keys('Lurke')
    time.sleep(2)
    
    addresstb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/div/textarea')
    addresstb.send_keys('2104 Tycos Dr')
    time.sleep(2)
    
    citytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/div/input')
    citytb.send_keys('Toronto')
    time.sleep(2)
    
    zipcodetb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    zipcodetb.send_keys('91001')
    time.sleep(2)
    
    phonetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[9]/td[2]/div/input')
    phonetb.send_keys('5061123344')
    time.sleep(2)
    
    faxtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[10]/td[2]/div/input')
    faxtb.send_keys('5061128899')
    time.sleep(2)
    
    celltb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[11]/td[2]/div/input')
    celltb.send_keys('5061112525')
    time.sleep(2)
    
    contactPersontb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[12]/td[2]/div/input')
    contactPersontb.send_keys('Cathlyn Storm')
    time.sleep(2)
    
    specialtytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[13]/td[2]/div/input')
    specialtytb.send_keys('sansa@gmail.com')
    time.sleep(2)
    
    licensetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[14]/td[2]/div/input')
    licensetb.send_keys('sansa@gmail.com')
    time.sleep(2)
    
    expDatetb = config.driver.find_element_by_xpath('//*[@id="expiration"]')
    expDatetb.send_keys('06072022')
    time.sleep(2)
    
    emailtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[17]/td[2]/div/input')
    emailtb.send_keys('sansa@gmail.com')
    time.sleep(2)
    
    aportal = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div[2]/table/tbody/tr[2]/td/table/tbody/tr[18]/td[2]/div/label/input')
    aportal.click()
    time.sleep(2)
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button')
    savebtn.click()
    
    
    
    