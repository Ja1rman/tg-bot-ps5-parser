# -*- coding: utf-8 -*-

import telebot
import requests
import traceback
import multiprocessing as mp
import time
import random

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@ps5parser'

ozonUrls = ["https://www.ozon.ru/context/detail/id/207702519/",
            "https://www.ozon.ru/context/detail/id/207702520/", 
            "https://www.ozon.ru/context/detail/id/178337786/",
            "https://www.ozon.ru/context/detail/id/178715781/"]

def ozon():
    session = requests.Session()
    while True:
        for url in ozonUrls:
            try:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
                response = session.get(url, headers=headers)
                r = response.text
                status = r[r.find('isAvailable')+13:]
                status = status[:status.find(',')]
                print(response.status_code)
                if status == 'true': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
                cookies = session.cookies.get_dict()
                for name in cookies:
                    if 'nlbi' in name or 'visid_incap' in name or 'incap_ses' in name:
                        session.cookies.set(name, '', domain='.ozon.ru')
            except: print(traceback.format_exc())

wildberriesUrls = ["https://www.wildberries.ru/15298664/product/data",
                   "https://www.wildberries.ru/15298663/product/data"]

def wildberries(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.json()
            status = r['value']['data']['addToBasketEnable']
            if status == 'True': bot.send_message(CHANNEL, 'https://www.wildberries.ru/catalog/' + r['value']['data']['rqCod1S'] + '/detail.aspx', disable_web_page_preview=True)
        except: print(traceback.format_exc())

goodsUrls = ["https://goods.ru/catalog/details/igrovaya-pristavka-sony-playstation-5-825gb-100026864564",
             "https://goods.ru/catalog/details/igrovaya-pristavka-sony-playstation-5-digital-edition-100027598944"]

def goods(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            r = r[r.find('"skuCode":"' + url[url.rfind('-')+1:]):]
            status = r[r.find('availableShops')+16:]
            status = status[:status.find(',')]
            if status != '0' and response.status_code == 200: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

gameparkUrls = ["https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5/",
                "https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5DigitalEdition/"]

def gamepark(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            if 'Нет в наличии' not in r and response.status_code == 200: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

technoparkUrls = ["https://spb.technopark.ru/igrovaya-pristavka-sony-playstation-5-cfi-1015a/"]

def technopark(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            if 'Нет в наличии' not in r and response.status_code == 200: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

c1Urls = ["http://www.1c-interes.ru/catalog/all6969/30328282/",
          "http://www.1c-interes.ru/catalog/all6969/30328284/"]

def c1():
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text       
            print('===', response.status_code)     
            if 'Перейти в корзину' in r: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
            time.sleep(random.randint(2, 5))
        except: print(traceback.format_exc())

def sony(url):
    while True:
        try: 
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                r = response.json()
                for id in r['prods']:
                    if int(r['prods'][id]['COUNT_IN_STOCK']) > 0:
                        bot.send_message(CHANNEL, 'https://store.sony.ru/product/' + id +'\nStock: ' + r['prods'][id]['COUNT_IN_STOCK'], disable_web_page_preview=True)
        except: print(traceback.format_exc())

if __name__ == "__main__":
    threads = []
    
    threads.append(mp.Process(target=ozon))
    threads[-1].start()
    
    for i in range(len(wildberriesUrls)):
        threads.append(mp.Process(target=wildberries, args=(wildberriesUrls[i],)))
        threads[-1].start()

    for i in range(len(goodsUrls)):
        threads.append(mp.Process(target=goods, args=(goodsUrls[i],)))
        threads[-1].start()

    for i in range(len(gameparkUrls)):
        threads.append(mp.Process(target=gamepark, args=(gameparkUrls[i],)))
        threads[-1].start()
    
    for i in range(len(technoparkUrls)):
        threads.append(mp.Process(target=technopark, args=(technoparkUrls[i],)))
        threads[-1].start()

    for i in range(len(c1Urls)):
        threads.append(mp.Process(target=c1, args=(c1Urls[i],)))
        threads[-1].start()

    threads.append(mp.Process(target=sony, args=('https://store.sony.ru/common/ajax_product.php?action=refresh_product_state&p_ids=[317406,317400]',)))
    threads[-1].start()
    
