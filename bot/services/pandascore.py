import requests
import os
from bot.core.bot_instance import pandascore
from datetime import datetime
import pytz

'''
Nome: FURIA fe | Acrônimo: FURIA.F | ID: 129384
Nome: FURIA Academy | Acrônimo: FURIA.A | ID: 126714
Nome: FURIA | Acrônimo: FURIA | ID: 124530

'''

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

def get_resultados():
    url = "https://api.pandascore.co/csgo/matches/past?filter[opponent_id]=124530&page=1&per_page=1"
    headers = {"Authorization": f"Bearer {pandascore}"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro {response.status_code}: {response.text}")
        return "⚠️ Erro ao buscar resultados da FURIA(CS2)."

    jogos = response.json()

    if not jogos:
        return "🚫 Nenhum resultado para a FURIA(CS2)"

    resposta = "🎮 *Resultados Jogos da FURIA (CS2):*\n\n"
    for jogo in jogos:
        torneio = jogo.get("serie", {}).get("full_name", "Torneio desconhecido")
        
        # Opponents e placar
        opponents = jogo.get("opponents", [])
        resultados = jogo.get("results", [])
        placar = []

        for i, op in enumerate(opponents):
            nome = op["opponent"]["name"]
            score = resultados[i]["score"] if i < len(resultados) else "?"
            placar.append(f"{nome} ({score})")

        placar_str = " vs ".join(placar) if placar else "Placar indefinido"

        # Data
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

        resposta += f"🏆 {torneio}\n📊 {placar_str}\n 🕒 {data_formatada}\n\n"

    return resposta
'''
def get_lineup():
    url = "https://api.pandascore.co/csgo/teams/124530"
    headers = {"Authorization": f"Bearer {pandascore}"}

    response = requests.get(url, headers=headers)
    data = response.json()

    jogadores = []
    coachs = []

    for player in data["players"]:
        nome = player.get("first_name") or ""
        pseudonimo = player.get("name") or ""
        nacionalidade = player.get("nationality") or ""
        idade = player.get("age") or ""

        jogador = {
            "Nome": nome,
            "Pseudônimo": pseudonimo,
            "Nacionalidade": nacionalidade,
            "Idade": idade
        }

        if player["role"] and "coach" in player["role"].lower():
            jogador["Posição"] = "Coach"
            coachs.append(jogador)
        elif "coach" in pseudonimo.lower() or pseudonimo.lower() == "guerri":
            jogador["Posição"] = "Coach"
            coachs.append(jogador)
        else:
            jogadores.append(jogador)

    return jogadores, coachs
'''