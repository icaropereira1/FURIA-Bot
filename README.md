
# 🐱‍👤 FURIA ChatBot

Um chatbot desenvolvido como parte do processo seletivo de estágio na equipe de desenvolvimento de software da FURIA Esports. O objetivo é criar uma aplicação interativa que responda perguntas sobre a organização e represente a identidade da FURIA de forma única, informativa e funcional.

---

## ⚙️ Tecnologias Utilizadas

- **Python** — Linguagem principal do projeto  
- **pyTelegramBotAPI** — Biblioteca para integração com a API do Telegram  
- **pandas** — Utilizado para leitura de tabelas HTML (Wikipedia)  
- **beautifulsoup4** — Web scraping (HLTV e outros)  
- **python-dotenv** - Utilizado para leitura e segurança das keys da API do Telegram  
- **pytz** - Utilizado para arrumar datas e horários

---

## 🧠 Funcionalidades

- `/start` — Boas-vindas e introdução ao FURIA Bot  
- `/loja` — Mostra os produtos disponíveis na loja oficial da FURIA  
- `/proximosjogos` — Exibe os próximos jogos do time CS2 da FURIA  
- `/resultados` — Exibe os resultados dos últimos 5 jogos da FURIA no CS2
- `/torcida` - Para inicar simulador de conversa de torcida
- `/lineup` — Mostra os jogadores e comissão técnica da equipe  
- `/titulos` — Lista os títulos conquistados pela FURIA no CS2  
- `/ativarnotificacao` — Ativa notificações automáticas sobre novos jogos  
- `/desativarnotificacao` — Cancela as notificações de novos jogos  


---

## 🚀 Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/icaropereira1/FURIA-Bot
cd FURIA-Bot
```

### 2. Configurar variáveis sensíveis

No arquivo `.env` coloque sua key da API do Telegram Bot e do PandaScore

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o bot

```bash
python -m bot.main
```

---

## 📁 Estrutura do Projeto

```
FURIA-Bot/
├── bot/
    ├── cache 
│   ├── core             # Importa configurações para funcionar framework
│   ├── handlers/        # Comandos do bot (/start, /loja, etc.)
│   ├── services/        # Funções auxiliares (pandascore, notificações)
│   ├── main.py          # Código principal do bot
│   └── __init__.py
├── requirements.txt     # Dependências
├── README.md            # Documentação
├── chat_notificacao     # Armazena chats que serão notificados
└── .env                 # Cadastro chaves de API
```

---

## 🛠️ Exemplo de Uso

**Usuário**: /proximosjogos  
**Bot**: 🔥Próximos jogos da FURIA:🔥

🏆 Campeonato: Astana 2025
🆚 TheMongolz
📅 10/05/2025 às 05:00
🔴 Assistir ao vivo (https://www.twitch.tv/PGL)

---

## 📌 Próximos Passos

- [ ] Criar um batepapo funcional que usa IA para responder o usuário
- [ ] Adicionar stats de players ao pagar por funcionalidade no PandaScore  
- [ ] Adicionar histórico de mensagens no modo bate-papo  
- [ ] Criar painel administrativo web para gerenciar notificações  
- [ ] Expandir para outras modalidades (Valorant, R6, Rocket League)  
- [ ] Suporte a múltiplos idiomas  


---

## ✒️ Autor

Desenvolvido por Ícaro Pereira Alves — estudante de Engenharia de Computação na UFG  
📧 Email: xicaroestudos@gmail.com  
🐙 GitHub: [@icaropereira1](https://github.com/icaropereira1)

---

## 🖤 FURIA

> "Somos uma família. Somos FURIA."

Este projeto é uma homenagem à dedicação, inovação e paixão que a FURIA representa no cenário dos esports.