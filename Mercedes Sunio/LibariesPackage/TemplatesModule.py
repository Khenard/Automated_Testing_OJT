from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from selenium.webdriver.support.select import Select



chromedriver = os.path.abspath('chromedriver.exe')
driver = webdriver.Chrome(chromedriver)

driver.get("https://qado.medisource.com")
driver.maximize_window()

usernametb = driver.find_element_by_id('loginemail').send_keys('superagent@geeksnest')
time.sleep(3)

passwordtb = driver.find_element_by_id('loginpassword').send_keys('Tester2021@')
time.sleep(3)

loginbtn = driver.find_element_by_xpath('/html/body/section/div/div[2]/form/div[6]/button')
loginbtn.click()
time.sleep(5)

driver.get("https://qado.medisource.com/narratives/templates")
time.sleep(5)

searchbtn = driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys('Automate')
time.sleep(5)

dropbtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div/div[2]/div/div/div/a/div')
dropbtn.click() 
time.sleep(5)
select = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div/div[2]/div/div/div/div/ul/li[2]')
select.click()
time.sleep(5)

nwtmplt = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[1]/a').click()
time.sleep(3)
ctgory = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/div/a').click()
time.sleep(3)
ctgorychoose = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/div/div/ul/li[2]')
ctgorychoose.click()
time.sleep(3)
dcpln = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[2]/td[2]/div/div/div/a').click()
time.sleep(3)
dcplnchoose = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[2]/td[2]/div/div/div/div/ul/li[3]').click()
time.sleep(3)
clcficatn = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[3]/td[2]/div/div/div').click()
time.sleep(3)
clcficatn = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[3]/td[2]/div/div/div/div/ul/li[2]').click()
#time.sleep(3)
ICD = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[4]/td[2]/input').send_keys('test1234')
#time.sleep(3)
title = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[5]/td[2]/input').send_keys('Chest pain')
#time.sleep(3)
Stper = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[7]/td/div/div[1]/textarea').send_keys('Lorem ipsum')
#time.sleep(3)
Steach = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[9]/td/div/div/div/table/tbody/tr/td/textarea').send_keys('Lorem ipsum')
#time.sleep(3)
subitem = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[9]/td/div/div/div/table/tbody/tr/td/div/textarea').send_keys('Lorem ipsum')
#time.sleep(3)
report = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[15]/td/div/div[1]/textarea').send_keys('Lorem Ipsum')
#time.sleep(3)
goal = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[17]/td/div/div[1]/textarea').send_keys('Lorem ipsum')
#time.sleep(3)
sev = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]').click()
time.sleep(5)

clacftn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[2]/div/ul/li[2]/a')
clacftn.click()
time.sleep(3)
clacisrch = driver.find_element_by_xpath('/html/body/section/section/data/div[2]/ui-view/div/div[1]/div/div[1]/div/div/div/input').send_keys('Artificial')
#time.sleep(5)

clacibtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div/div[2]/div/div/div')
clacibtn.click()
time.sleep(3)
clacichoose = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div/div[2]/div/div/div/div/ul/li[2]')
clacichoose.click()
time.sleep(3)

newclas = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[1]/a').click()
time.sleep(3)
categ = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/a')
categ.click()
time.sleep(3)
categchoose = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/div/ul/li[1]').click()
time.sleep(3)
classic = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[2]/td[2]/input').send_keys("Sample category")
#time.sleep(5)
general = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[4]/td/div/div[1]/div/table/tbody/tr/td/textarea').send_keys('Sample General Assessment')
#time.sleep(5)
nul = driver.find_element_by_xpath('/html/body/div[10]/button').click()
time.sleep(2)
savebtn = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button').click()
time.sleep(3)

ptgbtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[2]/div/ul/li[3]/a').click()
time.sleep(3)
ptgsearch = driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys('Diabetes')
time.sleep(3)
ptgdrop = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div[2]/div[2]/div/button/span[2]').click()
time.sleep(3)
ptgselect = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[1]/div[2]/div[2]/div/ul/li[3]/a').click()
time.sleep(3)

woundbtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[2]/div/ul/li[4]/a').click()
#time.sleep(3)
woundsrch = driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys('Test')
time.sleep(5)

newwoundbtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[1]/a').click()
time.sleep(2)
newfield = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/div/a').click()
fieldchoose = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/div/div/div/ul/li[10]').click()
entrynw = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[2]/td[2]/input').send_keys('sample test')
time.sleep(3)
adbtn = driver.find_element_by_xpath('/html/body/div[10]/button').click()
sevbtn = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button').click()

Mdobtn = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[2]/div/ul/li[5]/a').click()
time.sleep(3)
mdosrch = driver.find_element_by_xpath('//*[@id="searchbar__wrapper"]/div/input').send_keys('test')
time.sleep(3)
Newmdo = driver.find_element_by_xpath('//*[@id="content"]/data/div[1]/div/div/div[1]/a').click()
time.sleep(2)
mdotitle = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[1]/td[2]/div/input').send_keys('Sample MDO Title')
des = driver.find_element_by_xpath('//*[@id="content"]/data/div[2]/ui-view/div/div[2]/fieldset/ng-form/table/tbody/tr[2]/td[2]/textarea').send_keys('Sample Descrioption')
time.sleep(3)
btnsave = driver.find_element_by_xpath('//*[@id="titleNoteBar"]/tbody/tr/td/div/button[2]').click()
time.sleep(3)
back = driver.get('https://qado.medisource.com/dashboard')




 







