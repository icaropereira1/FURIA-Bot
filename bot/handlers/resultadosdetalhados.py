from bot.services.pandascore import get_resultados_detalhados, match_ids_por_chat
from telebot import formatting

def register(bot):
    @bot.message_handler(commands=['status_partida1', 'status_partida2', 'status_partida3', 'status_partida4', 'status_partida5'])
    def handle_resultados_detalhados(message):
        chat_id = message.chat.id
        comando = message.text.strip()
        
        try:
            index = int(comando[-1]) - 1  # Extrai o número do comando (1-5)
            match_ids = match_ids_por_chat.get(chat_id, [])
            
            if not match_ids:
                bot.reply_to(message, 
                    "❌ Nenhuma partida recente encontrada. Envie /resultados primeiro para carregar os jogos.")
                return
                
            if index < 0 or index >= len(match_ids):
                bot.reply_to(message,
                    f"❌ Partida não encontrada. Digite um número entre 1 e {len(match_ids)}.")
                return
                
            match_id = match_ids[index]
            detalhes = get_resultados_detalhados(match_id)
            
            # Envia a mensagem formatada como HTML
            bot.reply_to(message, detalhes, parse_mode="HTML")
            
            # Opcional: Envia imagem do jogo se disponível
            # if "image_url" in detalhes:
            #    bot.send_photo(chat_id, detalhes["image_url"])
            
        except Exception as e:
            error_msg = formatting.format_text(
                "⚠️ Ocorreu um erro ao processar sua requisição.",
                "Tente novamente mais tarde.",
                f"Erro: {str(e)}",
                separator="\n"
            )
            bot.reply_to(message, error_msg)
            # Log do erro para debug
            print(f"Erro em handle_resultados_detalhados: {str(e)}")