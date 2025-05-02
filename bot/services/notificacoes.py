import os

ARQUIVO_NOTIFICACOES = "chats_notificacao.txt"

def ativar_notificacao(chat_id):
    """Adiciona um chat_id à lista de notificações (se ainda não estiver lá)."""
    chat_id = str(chat_id)
    chats = obter_chats_notificacao()
    if chat_id not in chats:
        with open(ARQUIVO_NOTIFICACOES, "a") as f:
            f.write(f"{chat_id}\n")

def obter_chats_notificacao():
    """Lê os chats que ativaram notificação."""
    if not os.path.exists(ARQUIVO_NOTIFICACOES):
        return []
    with open(ARQUIVO_NOTIFICACOES, "r") as f:
        return [linha.strip() for linha in f if linha.strip()]

def desativar_notificacao(chat_id):
    """Remove um chat_id da lista de notificações."""
    chat_id = str(chat_id)
    chats = obter_chats_notificacao()
    if chat_id in chats:
        chats.remove(chat_id)
        with open(ARQUIVO_NOTIFICACOES, "w") as f:
            for id in chats:
                f.write(f"{id}\n")
