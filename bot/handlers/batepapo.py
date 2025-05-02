#import random
#from telebot import types

#def register(bot):
#    respostas_torcida = [
#        "FURIA CARALHO! 🔥", 
#        "VAMO DE PANTERA! 🐍",
#        "AQUI É FURIA PORRA! 💣",
#        "TACA O PAU NELES! 🔫"
#    ]

    # Comando /batepapo
#    @bot.message_handler(commands=['batepapo'])
#    def handle_batepapo(message):
#        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        markup.add("Quem é o capitão?", "Próximo jogo", "Sair")
#        bot.send_message(
#            message.chat.id,
#            "🤖 Modo bate-papo ativado! Pergunte sobre:\n- Jogadores\n- Próximos jogos\n- Títulos\nOu grite FURIA!",
#            reply_markup=markup
#        )

    # Respostas automáticas para torcida
#    @bot.message_handler(func=lambda m: any(kw in m.text.lower() for kw in ["furia", "vamo", "porra"]))
#    def handle_torcida(message):
#        bot.reply_to(message, random.choice(respostas_torcida))

    # Respostas para perguntas específicas
#    @bot.message_handler(func=lambda m: True)
#    def handle_mensagem(message):
#        resposta = gerar_resposta(message.text)
#        bot.reply_to(message, resposta)

#def gerar_resposta(pergunta):
##    pergunta = pergunta.lower()
#    faq = {
#        "quem é o capitão": "O capitão é Fallen (Gabriel Toledo)! 🎮🐍",
##       "títulos": "Veja a lista com /titulos! 🏆"
 #   }
    
#   for key in faq:
#        if key in pergunta:
#            return faq[key]
    
#    return random.choice([
#        "Não entendi, mas VAMO FURIA! 🔥",
#        "Pergunte sobre jogadores ou use /help"
#    ])