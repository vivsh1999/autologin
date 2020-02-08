from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://10.10.1.2:8090')

uname=driver.find_element_by_id('username')
uname.clear()
uname.send_keys("11701190_ce17")
pswd=driver.find_element_by_id('password')
pswd.clear()
pswd.send_keys("bond@007")
pswd.send_keys(Keys.ENTER)