from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cred import *

driver = webdriver.Firefox()
driver.get('http://10.10.1.2:8090')

uname=driver.find_element_by_id('username')
uname.clear()
uname.send_keys(getId())
pswd=driver.find_element_by_id('password')
pswd.clear()
pswd.send_keys(getPass())
pswd.send_keys(Keys.ENTER)