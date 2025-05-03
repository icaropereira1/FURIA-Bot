import time
import threading
from bot.services.pandascore import get_proximos_jogos
from datetime import datetime, timedelta
from bot.services.notificacoes import obter_chats_notificacao

# Armazena última notificação enviada (pode usar um arquivo depois se quiser persistir)
ultima_partida = None

def iniciar_monitoramento(bot):
    def monitorar():
        
        global ultima_partida
        while True:
            try:
                partidas = get_proximos_jogos()
                if partidas:
                    proxima = partidas[0]

                    # Checa se a partida mudou desde a última notificação
                    if proxima != ultima_partida:
                        ultima_partida = proxima

                        # Constrói a mensagem
                        mensagem = f"📢 NOVO JOGO DA FURIA!\n\n"
                        mensagem += f"🏆 Torneio: {proxima['campeonato']}\n"
                        mensagem += f"🆚 Adversário: {proxima['oponente']}\n"
                        mensagem += f"📅 Data: {proxima['data']}\n"
                        mensagem += f"⏰ Horário: {proxima['hora']}\n"
                        mensagem += f"🔗 Link: {proxima['link']}"

                        
                        for chat_id_salvo in obter_chats_notificacao():
                            try:
                                bot.send_message(chat_id_salvo, mensagem)
                            except Exception as e:
                                print(f"[Erro ao notificar {chat_id_salvo}]: {e}")

                time.sleep(3600)  # Verifica a cada hora

            except Exception as e:
                print(f"[Monitoramento] Erro: {e}")
                time.sleep(3600)

    threading.Thread(target=monitorar, daemon=True).start()

    