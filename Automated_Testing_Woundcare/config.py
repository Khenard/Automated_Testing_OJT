from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

file_path = os.path.abspath('./data/wound-images-week_7.png')
