# -*- coding: utf-8 -*-

import telebot
import requests
import time
import traceback
import threading

bot = telebot.TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@ozonparser'

urls = ["https://www.ozon.ru/context/detail/id/207702520/", 
        "https://www.ozon.ru/context/detail/id/216940493/",
        "https://www.ozon.ru/context/detail/id/178337786/",
        "https://www.ozon.ru/context/detail/id/173667655/",
        "https://www.ozon.ru/context/detail/id/178715781"]

def f(url):
    while True:
        try:
            for url in urls:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
                response = requests.get(url, headers=headers)
                print(response.status_code)
                r = response.text
                status = r[r.find('isAvailable')+13:]
                status = status[:status.find(',')]
                if status == 'true': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
        except: print(traceback.format_exc())

if __name__ == "__main__":
    for i in range(len(urls)):
        threads = []
        threads.append(threading.Thread(target=(f), args=(urls[i],)))
        threads[-1].start()
