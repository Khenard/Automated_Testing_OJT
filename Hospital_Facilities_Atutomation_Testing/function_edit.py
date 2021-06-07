from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
import config


def hospital_facility_edit():

    editbtn = config.driver.find_element_by_xpath('//*[@id="content"]/data/div/div[2]/div/table/tbody/tr[8]/td[5]/div/button/span').click()
    time.sleep(5)
    
    typeDdown = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div[1]/div/a/div/b')
    typeDdown.click()
    time.sleep(2)
    
    selectType = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div')
    selectType.click()
    
    nametb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[3]/td[2]/div/input')
    nametb.clear()
    time.sleep(2)
    nametb.send_keys('Fairview Hospital')
    time.sleep(2)
    
    addresstb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[4]/td[2]/div/input')
    addresstb.clear()
    time.sleep(2)
    addresstb.send_keys('2411  Tycos Dr')
    time.sleep(2)
    
    citytb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[5]/td[2]/div/input')
    citytb.clear()
    time.sleep(2)
    citytb.send_keys('Arizona')
    time.sleep(2)
    
    stateDdown = config.driver.find_element_by_xpath('//*[@id="state_chosen"]')
    stateDdown.click()
    time.sleep(2)
    
    selectState = config.driver.find_element_by_xpath('//*[@id="state_chosen"]/div')
    selectState.click()
    time.sleep(2)
    
    zip_codetb = config.driver.find_element_by_id('zipCode')
    zip_codetb.clear()
    time.sleep(2)
    zip_codetb.send_keys('96799')
    time.sleep(2)
    
    phonetb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[8]/td[2]/div/input')
    phonetb.clear()
    time.sleep(2)
    phonetb.send_keys('1025565211')
    time.sleep(2)
     
    faxtb = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[9]/td[2]/div/input')
    faxtb.clear()
    time.sleep(2)
    faxtb.send_keys('2035565211')
    time.sleep(2)
    
    con_person = config.driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/div/form/fieldset/div/table/tbody/tr[10]/td[2]/div/input')
    con_person.clear()
    time.sleep(2)
    con_person.send_keys('Julie Mayer')
    
    
    
    
    
    
    