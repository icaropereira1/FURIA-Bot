import telebot
from telebot import types
from bot.services.modobatepapo import get_resposta_ia

# Guarda quem está no modo de bate-papo

usuarios_ativos = set()

def register(bot):
    @bot.message_handler(commands=['batepapo'])
    def handle_batepapo(message):
        usuarios_ativos.add(message.chat.id)
        bot.reply_to(message, "🤖 Modo bate-papo ativado! Me pergunte algo sobre a FURIA ou CS2.")

    @bot.message_handler(commands=['sair'])
    def handle_sair(message):
        if message.chat.id in usuarios_ativos:
            usuarios_ativos.remove(message.chat.id)
            bot.reply_to(message, "🚪 Modo bate-papo desativado. Use /batepapo para ativar novamente.")
        else:
            bot.reply_to(message, "Você não está no modo bate-papo.")

    @bot.message_handler(func=lambda message: message.chat.id in usuarios_ativos)
    def handle_mensagem_ia(message):
        resposta = get_resposta_ia(message.text)
        bot.reply_to(message, resposta)
