def register(bot):
    @bot.message_handler(commands=['ativarnotificacao'])
    def handle_ativar_notificacao(msg):
        from bot.services.notificacoes import ativar_notificacao
        ativar_notificacao(msg.chat.id)
        bot.reply_to(msg, "🔔 Notificações ativadas! Você será avisado quando a FURIA tiver um novo jogo.")

    @bot.message_handler(commands=['desativarnotificacao'])
    def handle_desativar_notificacao(msg):
        from bot.services.notificacoes import desativar_notificacao
        desativar_notificacao(msg.chat.id)
        bot.reply_to(msg, "🔕 Notificações desativadas! Você não receberá alertas de jogos novos da FURIA.")
