import os
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()

bot = TeleBot(os.getenv("telegrambot_key"))
pandascore = os.getenv("PANDASCORE_API_KEY")