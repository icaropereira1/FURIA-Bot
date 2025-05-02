from bot.services.hltv import get_proximos_jogos

def register(bot):
    @bot.message_handler(commands=['proximosjogos'])
    def handle_proximos_jogos(message):
        jogos = get_proximos_jogos()

        resposta = "🎮 **Próximos Jogos da FURIA (CS2):**\n\n"
        resposta += "\n".join(f"- {jogo}" for jogo in jogos)

        bot.send_message(message.chat.id, resposta, parse_mode="Markdown")