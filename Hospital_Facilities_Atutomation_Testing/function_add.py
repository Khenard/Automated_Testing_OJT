from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def hospital_facility_add():

    newbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[1]/div/div[1]/a').click()
    time.sleep(5)
    
    typeDdown = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div[1]/div').click()
    time.sleep(2)
    
    selectType = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div/ul')
    selectType.click()
    time.sleep(2)
    
    stateDdown = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/a/div/b')
    stateDdown.click()
    time.sleep(2)
    
    selectState = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/div')
    selectState.click()
    time.sleep(2)
    
    nametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td[2]/div/input')
    nametb.send_keys('Westeria Hospital')
    time.sleep(2)
    
    addresstb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[4]/td[2]/div/input')
    addresstb.send_keys('2403  Tycos Dr')
    time.sleep(2)
    
    citytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[5]/td[2]/div/input')
    citytb.send_keys('Toronto')
    time.sleep(2)
    
    zip_codetb = config.driver.find_element_by_xpath('//*[@id="zipCode"]')
    zip_codetb.send_keys('96799')
    time.sleep(2)
    
    phonetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[8]/td[2]/div/input')
    phonetb.send_keys('1025565231')
    time.sleep(2)
     
    faxtb = config.driver.find_element_by_xpath(' //*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[9]/td[2]/div/input')
    faxtb.send_keys('2035565231')
    time.sleep(2)
    
    con_person = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[10]/td[2]/div/input')
    con_person.send_keys('Susie Mayer')
    time.sleep(2)
    
    savebtn  = config.driver.find_element_by_xpath('//*[@id="titleNoteBar"]/div/div/div/div/div/button[2]')
    savebtn.click()
    time.sleep(3)
    
    
    
    
    
    
    
    