#! python3
# 2048
# 2048 is a simple game where you combine tiles by sliding them up, down,
# left, or right with the arrow keys. You can actually get a fairly high score
# by repeatedly sliding in an up, right, down, and left pattern over and over
# again. Write a program that will open the game at https://gabrielecirulli
# .github.io/2048/ and keep sending up, right, down, and left keystrokes to
# automatically play the game.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os, requests, bs4


# maximize and disable infobars
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
options.add_argument('--disable-gpu')

url = 'https://gabrielecirulli.github.io/2048/'

driver = webdriver.Chrome(options=options, executable_path=r'D:\Python\others\chromedriver.exe')
driver.get(url)

htmlElem = driver.find_element_by_tag_name('html')

i = 0

def strategy1(webelem, num):
    i = 0
    while i < num:
        webelem.send_keys(Keys.RIGHT)
        webelem.send_keys(Keys.DOWN)

        webelem.send_keys(Keys.LEFT)
        webelem.send_keys(Keys.DOWN)
        i += 1


def strategy2(webelem, num):
    i = 0
    while i < num:
        webelem.send_keys(Keys.LEFT)
        i += 1

def strategy3(webelem, num):
    i = 0
    while i < num:
        webelem.send_keys(Keys.RIGHT)
        webelem.send_keys(Keys.UP)
        webelem.send_keys(Keys.LEFT)
        webelem.send_keys(Keys.DOWN)
        
        
        i += 1
    

while i < 10000:
    try:
        try_again = driver.find_element_by_class_name('retry-button')
        try_again.click()
    except:
        #strategy1(htmlElem, 50)
        #strategy2(htmlElem, 1)
        strategy3(htmlElem, 100)
        
    i += 1
