def register(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        texto = (
            "👋 Olá, seja bem-vindo ao *FURIA Bot*!\n\n"
            "Eu sou seu assistente oficial para tudo sobre a FURIA Esports. 🎮🔥\n\n"
            "Aqui estão alguns comandos que você pode usar:\n"
            "/lineup - Ver o elenco atual da FURIA 🐱‍👤\n"
            "/titulos - Conhecer os títulos conquistados 🏆\n"
            "/proximosjogos - Saber dos próximos jogos 📅\n"
            "/loja - Acessar a loja oficial da FURIA 🛒\n\n"
            "É só clicar no comando que quiser! 😎"
        )
        bot.send_message(message.chat.id, texto, parse_mode="Markdown")
