#coding:utf-8
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from headlessProxy import proxy_ext
from settings import TB, LOC_CHROMEDRIVER
USE_HEADLESS = TB['USE_HEADLESS']
USE_PORXY = TB["USE_PORXY"]
DICOUNT_LIST_NUM = TB["DICOUNT_LIST_NUM"]
URL = TB["URL"]

def get_tb_qianggou():
    try:
        #init webdriver
        d=[]
        opt = webdriver.ChromeOptions()
        if USE_HEADLESS:
            opt.add_argument('--disable-gpu')
            opt.add_argument('--headless')
        if USE_PORXY:
            opt.add_extension(proxy_ext())
        driver = webdriver.Chrome(executable_path=LOC_CHROMEDRIVER, chrome_options=opt)
        driver.get(URL)
        
        #go to current
        driver.find_element(By.XPATH, '//div[@data-status="current"]').click()
        time.sleep(3)
        
        #get endTime
        endTime = driver.find_element(By.XPATH, '//span[@class="clock"]').text
        
        #get qianggouInfo
        for i in range(1,DICOUNT_LIST_NUM):
            info = driver.find_element(By.XPATH, "//div[@class='qg-limit-list']/a[position()={}]".format(i)).text
            d.append(info)
        
        driver.close()
    except Exception as e:
        print(e)
    return d
    
    
if __name__ == '__main__':
    d = get_tb_qianggou()
    for i in d:
        print(i)