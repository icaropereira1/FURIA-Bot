from bot.core.bot_instance import bot
from telebot.types import Message
from bot.services.pandascore import get_resultados

def register(bot):
    @bot.message_handler(commands=["resultados"])
    def handle_proximos_jogos(message):
        resposta = get_resultados()
        bot.send_message(message.chat.id, resposta, parse_mode="Markdown")