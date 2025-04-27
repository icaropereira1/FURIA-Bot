from bot.services.bandeira import get_bandeira
from bot.services.wikipedia import get_lineup


def register(bot):
    @bot.message_handler(commands=['lineup'])
    def handle_lineup(message):
        jogadores, coachs = get_lineup()

        resposta = "🐱‍👤 **Lineup atual da FURIA (CS2):**\n\n"
        for jogador in jogadores:
            bandeira = get_bandeira(jogador["Nacionalidade"])
            resposta += f"- {bandeira} {jogador['Nome']} \"{jogador['Pseudônimo']}\"\n"

        resposta += "\n🎯 **Comissão Técnica:**\n\n"
        for coach in coachs:
            bandeira = get_bandeira(coach["Nacionalidade"])
            resposta += f"- {bandeira} {coach['Nome']} \"{coach['Pseudônimo']}\" ({coach['Posição']})\n"

        bot.reply_to(message, resposta, parse_mode="Markdown")