from bot.services.pandascore import get_proximos_jogos


def register(bot):
    @bot.message_handler(commands=['proximosjogos'])
    def handle_proximos_jogos(message):
        jogos = get_proximos_jogos()

        if not jogos:
            texto = "❌ Nenhum jogo encontrado."
        else:
            texto = "*🔥Próximos jogos da FURIA:🔥*\n\n"
            for jogo in jogos:
                texto += f"🏆 *Campeonato: *{jogo['campeonato']}\n"
                texto += f"🆚 {jogo['oponente']}\n"
                texto += f"📅 {jogo['data']} às {jogo['hora']}\n"
                if jogo["link"]:
                    texto += f"🔴 [Assistir ao vivo]({jogo['link']})\n"
                texto += "──────────────\n"

        bot.send_message(message.chat.id, texto, parse_mode="Markdown")