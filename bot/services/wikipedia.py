import pandas as pd

def get_lineup():
    tabelas = pd.read_html('https://pt.wikipedia.org/wiki/Furia_Esports#Elenco_atual')
    tabela_lineup = tabelas[2]

    tabela_lineup.columns = tabela_lineup.iloc[3]
    tabela_lineup = tabela_lineup[4:]
    tabela_lineup = tabela_lineup.dropna(how='any')

    jogadores = []
    coachs = []

    for _, row in tabela_lineup.iterrows():
        jogador = {
            "Pseudônimo": row['Pseudônimo'],
            "Nome": row['Nome'],
            "Nacionalidade": row['Nacionalidade'],
            "Posição": row['Posição']
        }

        if "Treinador" in row['Posição']:
            coachs.append(jogador)
        else:
            jogadores.append(jogador)

    return jogadores, coachs

def get_titulos():
    tabelas = pd.read_html('https://pt.wikipedia.org/wiki/Furia_Esports#Elenco_atual')
    tabela_titulos = tabelas[1]

    titulos_formatados = "🏆 *Títulos conquistados pela FURIA (CS:GO/CS2):*\n\n"
    for _, row in tabela_titulos.iterrows():
        ano = row.get("Ano", "")
        campeonato = row.get("Campeonato", "")
        posição = row.get("Posição", "")
        titulos_formatados += f"🔹 *{ano}* — {campeonato} ({posição})\n"

    return titulos_formatados
