from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
user = '' # Your username inside ''
pw = '' # Your password inside ''
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://el-gr.facebook.com/')
cookies = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]")
cookies.click()
username = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
username.click()
username.send_keys(user)
password = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
password.click()
password.send_keys(pw)
password.send_keys(Keys.RETURN)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[2]/span/div/div[1]").click()
time.sleep(1)
search = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/label/input")
search.click()
search.send_keys('') # Where will you send the message , inside ' '
time.sleep(2)
driver.find_element_by_partial_link_text("").click() # Where will you send the message , inside ""
time.sleep(2)
text = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[5]/div/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div")
text.click()
text.send_keys('Geia') # Your message inside ' '
time.sleep() # Seconds waiting before send the message inside ()
text.send_keys(Keys.RETURN)

