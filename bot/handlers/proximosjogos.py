from bot.services.pandascore import get_proximos_jogos


def register(bot):
    @bot.message_handler(commands=['proximosjogos'])
    def handle_proximos_jogos(message):
        resposta = get_proximos_jogos()
        bot.send_message(message.chat.id, resposta, parse_mode="Markdown")

        
