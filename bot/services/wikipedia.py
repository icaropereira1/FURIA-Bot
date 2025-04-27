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

    # Converte a tabela pra Markdown
    markdown_table = tabela_titulos.to_markdown(index=False)

    return markdown_table