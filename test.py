import webbrowser
import win32api
import os
from time import sleep
from selenium import webdriver

# put the driver in the dir of [dist]

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
browser.get('http://www.baidu.com')


# webbrowser.open("http://www.jitaba.cn/pic/7179.html",1)
#
# sleep(10)
# win32api.keybd_event(40,0,0,0)
#
# sleep(1)
# win32api.keybd_event(40,0,0,0)
# sleep(1)
#
# win32api.keybd_event(40,0,0,0)
