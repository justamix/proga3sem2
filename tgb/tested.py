import telebot
import config
import logging
from telebot import types
import requests
from bs4 import BeautifulSoup as BS
from random import randint
#import schedule
#import time
#import threading

bot = telebot.TeleBot(config.TOKEN)

logging.basicConfig(level=logging.INFO)

def parsing(URL):
    r = requests.get(URL)
    html = BS(r.content, 'html.parser') 
    anekdot_text = html.find('div', class_ = 'text').get_text(strip = True)
    return anekdot_text

def sent_message():
    random_id = randint(10000, 11000)
    URL = f"https://www.anekdot.ru/id/{random_id}/"
    txt = parsing(URL)
     

# Стартовое приветствие
@bot.message_handler(commands = ['start'])
def start_message(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Анeкдот")
#    item2 = types.KeyboardButton("Анекдот каждый час")
    markup.add(item1)
#    markup.add(item2)
    
    #приветствие со стикером
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}!\nМеня зовут {bot.get_me().first_name}", reply_markup = markup)
    with open('C:/Users/fmmf2/OneDrive/Рабочий стол/лабы 3 сем/tgb/sticker.webp', 'rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)

@bot.message_handler(content_types=['text'])
def another_message(message):
    #обработка запроса Анекдот
    if message.text == "Анeкдот":
        random_id = randint(10000, 11000)
        URL = f"https://www.anekdot.ru/id/{random_id}/"
        anekdot_text = parsing(URL)
        bot.send_message(message.chat.id, anekdot_text)
#    if message.text == "Анекдот каждый час":
#        a = threading.Thread(target = parsing, args=(URL,))
#        a.start()
if __name__ == "__main__":
    
    bot.polling(non_stop = True)