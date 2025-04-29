from bot.services.wikipedia import get_titulos

def register(bot):
    @bot.message_handler(commands=['titulos'])
    def handle_titulos(msg):
        resposta = get_titulos()
        bot.send_message(msg.chat.id, resposta, parse_mode="Markdown")