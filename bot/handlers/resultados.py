from bot.services.pandascore import get_resultados, match_ids_por_chat

def register(bot):
    @bot.message_handler(commands=['resultados'])
    def handle_resultados(message):
        chat_id = message.chat.id
        resposta, match_ids = get_resultados()  # Desempacota a tupla
        match_ids_por_chat[chat_id] = match_ids  # Armazena para uso futuro
        bot.reply_to(message, resposta, parse_mode="HTML")