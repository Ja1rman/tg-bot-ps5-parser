# -*- coding: utf-8 -*-

from telebot import TeleBot 
import requests
import time

bot = TeleBot('1680508706:AAGu_zrjj1X9BzYMNUhb3CW1E7ABey4Ft8Q')
CHANNEL = '@ozonparser'

urls = ["https://www.ozon.ru/context/detail/id/207702520/", 
       "https://www.ozon.ru/context/detail/id/216940493/",
       "https://www.ozon.ru/context/detail/id/178337786/",
       "https://www.ozon.ru/context/detail/id/173667655/"]

if __name__ == "__main__":
    while True:
        try:
            for url in urls:
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"} 
                response = requests.get(url, headers=headers).text
                status = response[response.find('isAvailable')+13:]
                status = status[:status.find(',')]
                if status == 'true': bot.send_message(CHANNEL, url, disable_web_page_preview=True)
            time.sleep(0.3)
        except: pass
