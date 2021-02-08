# -*- coding: utf-8 -*-

import telebot
import requests
import time
import traceback
import threading

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@ozonparser'

ozonUrls = ["https://www.ozon.ru/context/detail/id/207702519/",
        "https://www.ozon.ru/context/detail/id/207702520/", 
        "https://www.ozon.ru/context/detail/id/216940493/",
        "https://www.ozon.ru/context/detail/id/178337786/",
        "https://www.ozon.ru/context/detail/id/173667655/",
        "https://www.ozon.ru/context/detail/id/178715781"]

wildberriesUrls = ["https://www.wildberries.ru/catalog/15298664/detail.aspx",
                   "https://www.wildberries.ru/catalog/15298663/detail.aspx"]

def ozon(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            print(response.status_code)
            r = response.text
            status = r[r.find('isAvailable')+13:]
            status = status[:status.find(',')]
            if status == 'true': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

def wildberries(url):
    while True:
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
            response = requests.get(url, headers=headers)
            print(response.status_code)
            r = response.text
            status = r[r.find('isSoldOut"')+11:]
            status = status[:status.find(',')]
            if status == 'false': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

if __name__ == "__main__":
    threads = []
    for i in range(len(ozonUrls)):
        threads.append(threading.Thread(target=(ozon), args=(ozonUrls[i],)))
        threads[-1].start()
    
    for i in range(len(wildberriesUrls)):
        threads.append(threading.Thread(target=(wildberries), args=(wildberriesUrls[i],)))
        threads[-1].start()
