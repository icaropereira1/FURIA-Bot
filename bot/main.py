import telebot

bot = telebot.TeleBot('8160505498:AAEwwFnFz-UlNYlmKhU_rX7_Zzoyz03iHH4')

from bot.handlers import start, loja, lineup, proximosjogos, titulos

# Registra handlers
start.register(bot)
loja.register(bot)
lineup.register(bot)
proximosjogos.register(bot)
titulos.register(bot)

print("Bot iniciado...")
bot.polling()