# 2048 project of Chapter 12 of the book
# By  JITHIN JOHN
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = driver.find_element_by_tag_name('html')
i=0
while i==0:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
