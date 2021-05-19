from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os

#Configure web driver
chromedriver = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()

driver.get("https://qado.medisource.com/patient")