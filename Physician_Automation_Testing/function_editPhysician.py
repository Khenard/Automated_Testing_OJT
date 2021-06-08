from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config



def physician_edit():

    editbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div[1]/table/tbody/tr[9]/td[5]/div/button[2]')
    editbtn.click()
    time.sleep(5)
    
    npitb = config.driver.find_element_by_xpath('//*[@id="npiId"]/td[2]/div/input')
    npitb.clear()
    time.sleep(2)
    npitb.send_keys('1558444233')
    time.sleep(5)
    
    fnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]/div/input')
    fnametb.clear()
    time.sleep(2)
    fnametb.send_keys('Catlyn')
    time.sleep(2)
    
    mnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/div/input')
    mnametb.clear()
    time.sleep(2)
    mnametb.send_keys('Gambyss')
    time.sleep(2)
    
    lnametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[4]/td[2]/div/input')
    lnametb.clear()
    time.sleep(2)
    lnametb.send_keys('Lurkes')
    time.sleep(2)
    
    addresstb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[5]/td[2]/div/textarea')
    addresstb.clear()
    time.sleep(2)
    addresstb.send_keys('2112 Tycos Dr')
    time.sleep(2)
    
    citytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[6]/td[2]/div/input')
    citytb.clear()
    time.sleep(2)
    citytb.send_keys('Quebec')
    time.sleep(2)
    
    zipcodetb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    zipcodetb.clear()
    time.sleep(2)
    zipcodetb.send_keys('91001')
    time.sleep(2)
    
    phonetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[9]/td[2]/div/input')
    phonetb.clear()
    time.sleep(2)
    phonetb.send_keys('5061123340')
    time.sleep(2)
    
    faxtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[10]/td[2]/div/input')
    faxtb.clear()
    time.sleep(2)
    faxtb.send_keys('5061128890')
    time.sleep(2)
    
    celltb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[11]/td[2]/div/input')
    celltb.clear()
    time.sleep(2)
    celltb.send_keys('5061112520')
    time.sleep(2)
    
    contactPersontb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[12]/td[2]/div/input')
    contactPersontb.clear()
    time.sleep(2)
    contactPersontb.send_keys('Lyn Stormborn')
    time.sleep(2)
    
    specialtytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[13]/td[2]/div/input')
    specialtytb.clear()
    time.sleep(2)
    specialtytb.send_keys('Family Medicine')
    time.sleep(2)
    
    licensetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[14]/td[2]/div/input')
    licensetb.clear()
    time.sleep(2)
    licensetb.send_keys('2300326564')
    time.sleep(2)
    
    expDatetb = config.driver.find_element_by_xpath('//*[@id="expiration"]')
    expDatetb.clear()
    time.sleep(2)
    expDatetb.send_keys('06072023')
    time.sleep(2)
    
    emailtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[17]/td[2]/div/input')
    emailtb.clear()
    time.sleep(2)
    emailtb.send_keys('cathlyn@gmail.com')
    time.sleep(2)
    
    aportal = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td/table/tbody/tr[18]/td[2]/div/label/input')
    aportal.click()
    time.sleep(2)
    
    savebtn = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button')
    savebtn.click()
    