import requests
from bs4 import BeautifulSoup

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
            return ["Nenhum próximo jogo encontrado."]

        for match in matches[:5]:  # Pega no máximo 5 próximos jogos
            opponent = match.select_one('.matchTeamName').text.strip()
            time = match.select_one('.matchTime').text.strip()
            event = match.select_one('.matchEventName').text.strip()

            jogo = f"{time} - FURIA vs {opponent} ({event})"
            jogos.append(jogo)

        return jogos

    except Exception as e:
        print(f"Erro ao buscar próximos jogos: {e}")
        return ["Erro ao buscar jogos."]
