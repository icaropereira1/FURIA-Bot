from bot.services.wikipedia import get_titulos

def register(bot):

    @bot.message_handler(commands=['titulos'])
    def handle_titulos(msg):
        titulos_data = get_titulos()

        resposta_formatada = f"*Títulos da FURIA:*\n```markdown\n{titulos_data}\n```"

        bot.send_message(
            msg.chat.id,
            resposta_formatada,
            parse_mode="Markdown"
        )