#!python3
#coding:utf-8

LOC_CHROMEDRIVER=r'd:\webdriver\chromedriver.exe'

JD=dict(
    URL='https://www.jd.com',
    USE_HEADLESS=0,
    USE_PORXY=0,
    DICOUNT_LIST_NUM=22,
    )
    
TB=dict(
    URL='https://qiang.taobao.com',
    USE_HEADLESS=0,
    USE_PORXY=0,
    DICOUNT_LIST_NUM=50,
    )
    
headlessProxy=dict(
    LOC_PORXYPLUSIN=r'./proxy_auth_plugin.zip',
    HOST="X.X.X.X",
    PORT="",
    USERNAME="",
    PASSWORD="",
    )