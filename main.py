# -*- coding: utf-8 -*-

import telebot
import requests
import traceback
import threading

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@ps5parser'

ozonUrls = ["https://www.ozon.ru/context/detail/id/207702519/",
        "https://www.ozon.ru/context/detail/id/207702520/", 
        "https://www.ozon.ru/context/detail/id/216940493/",
        "https://www.ozon.ru/context/detail/id/178337786/",
        "https://www.ozon.ru/context/detail/id/173667655/",
        "https://www.ozon.ru/context/detail/id/178715781"]

def ozon(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            status = r[r.find('isAvailable')+13:]
            status = status[:status.find(',')]
            if status == 'true': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

wildberriesUrls = ["https://www.wildberries.ru/catalog/15298664/detail.aspx",
                   "https://www.wildberries.ru/catalog/15298663/detail.aspx"]

def wildberries(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            r = response.text
            status = r[r.find('isSoldOut"')+11:]
            status = status[:status.find(',')]
            if status == 'false': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
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
            print(status)
            if status != '0' and response.status_code == 200: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

gameparkUrls = ["https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5/",
                "https://www.gamepark.ru/playstation5/console/IgrovayakonsolSonyPlayStation5DigitalEdition/"]

def gamepark(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            print(response.status_code)
            r = response.text
            if 'Нет в наличии' not in r and response.status_code == 200: bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

if __name__ == "__main__":
    threads = []
    for i in range(len(ozonUrls)):
        threads.append(threading.Thread(target=(ozon), args=(ozonUrls[i],)))
        threads[-1].start()
    
    for i in range(len(wildberriesUrls)):
        threads.append(threading.Thread(target=(wildberries), args=(wildberriesUrls[i],)))
        threads[-1].start()

    for i in range(len(goodsUrls)):
        threads.append(threading.Thread(target=(goods), args=(goodsUrls[i],)))
        threads[-1].start()

    for i in range(len(gameparkUrls)):
        threads.append(threading.Thread(target=(gamepark), args=(gameparkUrls[i],)))
        threads[-1].start()
