import os
import telebot
from telebot import types
from passwords import API_KEY

bot = telebot.TeleBot(API_KEY)

imageFile1 = f"ASKA.jpg"
imageFile2 = f"RAY.jpg"
audioFile = f"BRUH.mp3"

@bot.message_handler(commands=['SendAska'])
def greet(message):
    img = open(imageFile1, 'rb')
    bot.send_photo(message.chat.id, img, caption="TEST")

@bot.message_handler(commands=['SendRay'])
def greet(message):
    img = open(imageFile2, 'rb')
    bot.send_photo(message.chat.id, img, caption="TEST")

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

@bot.message_handler(commands=['SendBruh'])
def hello(message):
    audio = open(audioFile, 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()


bot.polling()
