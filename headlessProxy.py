from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import zipfile

from settings import headlessProxy
LOC_PORXYPLUSIN = headlessProxy['LOC_PORXYPLUSIN']
HOST = headlessProxy["HOST"]
PORT = ["PORT"]
USERNAME = ["USERNAME"]
PASSWORD = ["PASSWORD"]

def proxy_ext(porxy_path=LOC_PORXYPLUSIN):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "http",
                host: "XXX.XXX.XXX.XXX",
                port: parseInt(XXXX)
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "XXXXXXXXX",
                password: "XXXXXXXXX"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """.format(
    host=HOST,
    port=PORT,
    username=USERNAME, 
    password=PASSWORD
    )


    with zipfile.ZipFile(porxy_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return porxy_path
