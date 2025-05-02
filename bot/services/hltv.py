import requests
from bs4 import BeautifulSoup

# Comentando o comando de monitoramento do site HLTV para testar o a notificação 
'''
def get_proximos_jogos():
    url = 'https://www.hltv.org/team/8297/furia#tab-matchesBox'

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        jogos = []

        matches = soup.select('.upcomingMatch')

        if not matches:
            return []

        for match in matches[:5]:  # Pega no máximo 5 próximos jogos
            opponent_tag = match.select_one('.matchTeam.team2 .matchTeamName') or match.select_one('.matchTeamName')
            opponent = opponent_tag.text.strip() if opponent_tag else "Desconhecido"

            time_tag = match.select_one('.matchTime')
            hora = time_tag.text.strip() if time_tag else "Horário desconhecido"

            event_tag = match.select_one('.matchEventName')
            campeonato = event_tag.text.strip() if event_tag else "Evento desconhecido"

            date_attr = match.get("data-unix")  # timestamp em milissegundos
            if date_attr:
                from datetime import datetime
                timestamp = int(date_attr) // 1000
                data = datetime.utcfromtimestamp(timestamp).strftime("%d/%m/%Y")
            else:
                data = "Data desconhecida"

            link_tag = match.select_one('a')
            link = f"https://www.hltv.org{link_tag['href']}" if link_tag else "https://hltv.org"

            jogo = {
                'campeonato': campeonato,
                'oponente': opponent,
                'data': data,
                'hora': hora,
                'link': link
            }

            jogos.append(jogo)

        return jogos

    except Exception as e:
        print(f"Erro ao buscar próximos jogos: {e}")
        return []

'''            
def get_proximos_jogos():
    return [{
        'campeonato': 'Torneio Teste',
        'oponente': 'Time Fake',
        'data': '10/05/2025',
        'hora': '19:00',
        'link': 'https://furia.gg/test'
    }]
