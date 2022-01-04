import json
from time import sleep as s
import requests, os, subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from time import sleep as s
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


def send_sms():
    from twilio.rest import Client
    account_sid = 'AC67d1437cea8593339dce6ec20c4eeeb3'
    auth_token = '60e2616f01b750c78efd6d44022a8210'
    client = Client(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='THE ITEM IS ADDED TO YOUR CART GOGOGOGO',
        from_='+18592953746',
        to='+18137532081')


options = Options()
home_dir = os.getenv('USERPROFILE')
options.add_argument('start-maximized')
options.add_argument('log-level=3')
options.add_argument(
    f"user-data-dir={home_dir}\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
)
link = 'https://www.bestbuy.com/api/tcfb/model.json?paths=%5B%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22storeId%22%2C%22stores%22%2C852%2C%5B%22status%22%2C%22storeType%22%5D%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6432445%2C%22descriptions%22%2C%5B%22long%22%2C%22shortSynopsis%22%5D%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6432445%2C%22images%22%2C%220%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6432445%2C%22names%22%2C%22short%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v1%22%2C%22sites%22%2C%22skuId%22%2C6432445%2C%22sites%22%2C%22bbypres%22%2C%22relativePdpUrl%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22product%22%2C%22skus%22%2C6432445%2C%5B%22seasonDetails%22%2C%22videoDetails%22%5D%2C0%2C%22synopsis%22%5D%2C%5B%22shop%22%2C%22magellan%22%2C%22v2%22%2C%22hierarchy%22%2C%22skus%22%2C6432445%2C%22hierarchies%22%2C%22bbypres%22%2C%7B%22from%22%3A0%2C%22to%22%3A1%7D%2C%22href%22%5D%2C%5B%22shop%22%2C%22buttonstate%22%2C%22v5%22%2C%22item%22%2C%22skus%22%2C6432445%2C%22conditions%22%2C%22NONE%22%2C%22destinationZipCode%22%2C96939%2C%22storeId%22%2C852%2C%22context%22%2C%22cyp%22%2C%22addAll%22%2C%22false%22%5D%2C%5B%22shop%22%2C%22recommendations%22%2C%22api%22%2C%22list%22%2C%22srcs%22%2C%22dotcom-l%22%2C%22skuIds%22%2C6432445%2C%22plmts%22%2C%22cyp%22%2C%22pageSizes%22%2C10%2C%22apiKeys%22%2C%22D50%22%2C%22cyp%22%2C%22ep%22%5D%2C%5B%22shop%22%2C%22recommendations%22%2C%22api%22%2C%22list%22%2C%22srcs%22%2C%22dotcom-l%22%2C%22skuIds%22%2C6432445%2C%22plmts%22%2C%22cyp%22%2C%22pageSizes%22%2C10%2C%22apiKeys%22%2C%22D50%22%2C%22cyp%22%2C%22_entries%22%2C%7B%22from%22%3A0%2C%22to%22%3A9%7D%2C%5B%22ep%22%2C%22id%22%2C%22rank%22%5D%5D%5D&method=get'
headers = {
    'authority': 'www.bestbuy.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74',
    'accept': '*/*',
    'referer':
    'https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445&intl=nosplash',
    'sec-fetch-dest': 'empty',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors'
}
if getattr(sys, 'frozen', False):
    chrome_driver = os.path.join(sys._MEIPASS, 'chromedriver.exe')
else:
    chrome_driver = 'chromedriver.exe'
with open('./log.txt', 'w', encoding='utf-8') as (file):
    file.write(
        'Bot started\nParsing the request\nYou can now wait and chillax!\n\n')
os.startfile('log.txt')


def check():
    while True:
        with open('./log.txt', 'a', encoding='utf-8') as (file):
            file.write('Bot is making new request...\n')
        response = requests.get(link, headers=headers)
        response_formatted = json.load(
            response.content.decode('utf-8-sig').encode('utf-8'))
        with open('./log.txt', 'a', encoding='utf-8') as (file):
            file.write('Bot is parsing the new request...\n')
        sold_out = response_formatted['jsonGraph']['shop']['buttonstate'][
            'v5']['item']['skus']['6432445']['conditions']['NONE'][
                'destinationZipCode']['96939']['storeId']['852']['context'][
                    'cyp']['addAll']['false']['value'][
                        'buttonStateResponseInfos'][0][
                            'buttonState'] == 'SOLD_OUT'
        if sold_out:
            s(1)
            with open('./log.txt', 'a', encoding='utf-8') as (file):
                file.write('The product is still sold out!\n')
        else:
            with open('./log.txt', 'w', encoding='utf-8') as (file):
                file.write('PRODUCT IS AVAILABLE\n Bot is running')
            driver = webdriver.Chrome(executable_path=chrome_driver,
                                      options=options)
            driver.get(
                'https://www.bestbuy.com/site/asus-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-strix-graphics-card-black/6432445.p?skuId=6432445&intl=nosplash'
            )
            WebDriverWait(driver,
                          5).until(lambda x: x.find_element_by_class_name(
                              'add-to-cart-button')).click()
            send_sms()


check()