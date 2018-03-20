#coding:utf-8
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from headlessProxy import proxy_ext
from settings import JD, LOC_CHROMEDRIVER
USE_HEADLESS = JD['USE_HEADLESS']
USE_PORXY = JD["USE_PORXY"]
DICOUNT_LIST_NUM = JD["DICOUNT_LIST_NUM"]
URL = JD["URL"]

clickTime=int(DICOUNT_LIST_NUM%4)
flash_deals_clstag=r'h|keycount|core|seckill_b{}'

def get_jd_flashDeals():
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
        
        #get endTime
        endTime = driver.find_element(By.CLASS_NAME, 'sk_cd').text
        d.append(endTime)
        
        #get change button
        button = driver.find_element(By.XPATH, '//i[@clstag="h|keycount|core|seckill_sr"]')

        #get discount info
        for i in range(1,DICOUNT_LIST_NUM+1):
            clstag = gen_clstag(flash_deals_clstag, i)
            info = driver.find_element(By.XPATH, '//a[@clstag="{}"]'.format(clstag)).text
            print(info)
            re_info = re.split('\n', info)
            d.append(re_info)
            
            if i%4==0:
                button.click()
                time.sleep(2)
        driver.close()
    except Exception as e:
        print(e)
    return d
    
def gen_clstag(origin, num):
    if num<10:
        j='0'+str(num)
    else:
        j=str(num)
    return origin.format(j)
    
if __name__ == '__main__':
    d = get_jd_flashDeals()
    for i in d:
        print(i)