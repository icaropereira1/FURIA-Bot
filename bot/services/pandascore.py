import requests
import os
from bot.core.bot_instance import pandascore, bot
from datetime import datetime
import pytz

def get_proximos_jogos():
    url = "https://api.pandascore.co/csgo/matches/upcoming?filter[opponent_id]=124530"
    headers = {"Authorization": f"Bearer {pandascore}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    jogos = response.json()
    proximos = []

    for jogo in jogos:
        data_iso = jogo.get("begin_at")
        if data_iso:
            dt_utc = pytz.utc.localize(datetime.fromisoformat(data_iso.replace("Z", "")))
            dt_brt = dt_utc.astimezone(pytz.timezone("America/Sao_Paulo"))
            data_formatada = dt_brt.strftime("%d/%m/%Y")
            hora_formatada = dt_brt.strftime("%H:%M")
        else:
            data_formatada = "Indefinida"
            hora_formatada = "Indefinido"

        campeonato = jogo.get("serie", {}).get("full_name", "Torneio indefinido")
        adversario = [op["opponent"]["name"] for op in jogo.get("opponents", []) if op["opponent"]["name"] != "FURIA"]
        adversario = adversario[0] if adversario else "Adversário indefinido"

        # NOVO: pega o link da stream principal se existir
        streams = jogo.get("streams_list", [])
        stream_principal = next((s["raw_url"] for s in streams if s.get("main")), None)
        link = stream_principal 

        proximos.append({
            "campeonato": campeonato,
            "oponente": adversario,
            "data": data_formatada,
            "hora": hora_formatada,
            "link": link
        })

    return proximos

match_ids_por_chat = {}

def get_resultados(chat_id=None):
    url = "https://api.pandascore.co/csgo/matches/past?filter[opponent_id]=124530&page=1&per_page=5"
    headers = {"Authorization": f"Bearer {pandascore}"}

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return "⚠️ Erro ao buscar resultados da FURIA(CS2).", []

    jogos = response.json()

    if not jogos:
        return "🚫 Nenhum resultado para a FURIA(CS2)", []

    resposta = "🎮 <b>Resultados Jogos da FURIA (CS2):</b>\n\n"
    match_ids = []

    for i, jogo in enumerate(jogos, start=1):
        torneio = jogo.get("serie", {}).get("full_name", "Torneio desconhecido")
        opponents = jogo.get("opponents", [])
        resultados = jogo.get("results", [])
        placar = []

        for j, op in enumerate(opponents):
            nome = op["opponent"]["name"]
            score = resultados[j]["score"] if j < len(resultados) else "?"
            placar.append(f"{nome} ({score})")

        placar_str = " vs ".join(placar) if placar else "Placar indefinido"
        match_id = jogo.get("id")
        match_ids.append(match_id)

        data_iso = jogo.get("begin_at")
        if data_iso:
            try:
                utc = pytz.utc
                br_tz = pytz.timezone("America/Sao_Paulo")
                dt_utc = utc.localize(datetime.fromisoformat(data_iso.replace("Z", "")))
                dt_brt = dt_utc.astimezone(br_tz)
                data_formatada = dt_brt.strftime("%d/%m/%Y %H:%M")
            except ValueError:
                data_formatada = data_iso
        else:
            data_formatada = "Data indefinida"

        resposta += (
            f"🏆 <b>Torneio:</b>{torneio}\n"
            f"📊 {placar_str}\n"
            f"🕒 {data_formatada}\n"
            f"    /status_partida{i}\n\n"
        )

    return resposta, match_ids


def get_resultados_detalhados(match_id):
    url = f"https://api.pandascore.co/matches/{match_id}"
    headers = {"Authorization": f"Bearer {pandascore}"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        dados = response.json()
        
        # Processamento dos dados
        torneio = dados.get("serie", {}).get("full_name", "Torneio desconhecido")
        opponents = dados.get("opponents", [])
        resultados = dados.get("results", [])
        games = dados.get("games", [])
        
        # Placar principal
        placar = []
        for i, op in enumerate(opponents):
            nome = op["opponent"]["name"]
            score = resultados[i]["score"] if i < len(resultados) else "?"
            placar.append(f"{nome} ({score})")
        
        # Detalhes por mapa
        detalhes_mapas = []
        for game in games:
            if game.get("complete"):
                mapa = f"Mapa {game['position']}"
                duracao = f"{game['length']//60} min" if game.get("length") else ""
                vencedor = next((op["opponent"]["name"] for op in opponents 
                               if op["opponent"]["id"] == game["winner"]["id"]), "?")
                detalhes_mapas.append(f"• {mapa}: {vencedor} {duracao}")
        
        # Streams
        streams = "\n".join(
            f"🔴 {s['language'].upper()}: {s['raw_url']}" 
            for s in dados.get("streams_list", []) 
            if s.get("main")
        )
        
        # Formatação da mensagem
        mensagem = (
            f"<b>🎮 {dados.get('name', 'Partida')}</b>\n"
            f"🏆 <b>Torneio:</b> {torneio}\n"
            f"📊 <b>Placar Final:</b> {' vs '.join(placar)}\n\n"
            f"<b>🗺 Detalhes por Mapa:</b>\n" + "\n".join(detalhes_mapas) + "\n\n"
            f"⏱ <b>Duração Total:</b> {len(games)} mapas\n"
            f"📅 <b>Data:</b> {dados.get('begin_at', '?')}\n\n"
            f"<b>📺 Transmissão Oficial:</b>\n{streams if streams else 'Nenhum link disponível'}\n\n"
            f"#FURIA #CS2"
        )
        
        return mensagem
    
    except Exception as e:
        return f"⚠️ Erro ao buscar detalhes: {str(e)}"