import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('telegrambot_key'))

from bot.handlers import start, loja, lineup, proximosjogos, titulos, batepapo, ativar_des_notificações
from bot.services.monitoramento import iniciar_monitoramento

iniciar_monitoramento(bot)

# Registra handlers
start.register(bot)
loja.register(bot)
lineup.register(bot)
proximosjogos.register(bot)
titulos.register(bot)
ativar_des_notificações.register(bot)

print("Bot iniciado...")
bot.polling()