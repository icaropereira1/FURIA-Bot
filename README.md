# 🐱‍👤 FURIA ChatBot

![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Chatbot desenvolvido como parte do processo seletivo de estágio na equipe de desenvolvimento de software da **FURIA Esports**. O objetivo é criar uma aplicação interativa que responda perguntas sobre a organização e represente a identidade da FURIA de forma única, informativa e funcional.

---

## 🎥 Demonstração

![Demonstração do Bot](https://user-images.githubusercontent.com/seu-usuario/demo-furia-bot.gif) <!-- Substitua pelo link do seu GIF ou screenshot -->

---

## 🔧 Requisitos

- Python 3.10+
- Conta no [Telegram](https://telegram.org/) e na [PandaScore](https://www.pandascore.co)
- Ambiente virtual (opcional, mas recomendado)

---

## ⚙️ Tecnologias Utilizadas

- **Python** — Linguagem principal do projeto  
- **pyTelegramBotAPI** — Integração com a API do Telegram  
- **pandas** — Leitura de tabelas HTML (ex: Wikipedia)  
- **beautifulsoup4** — Web scraping (HLTV e outros)  
- **python-dotenv** — Gerenciamento seguro das chaves da API  
- **pytz** — Manipulação de datas e horários com timezone

---

## 🧠 Funcionalidades

- `/start` — Mensagem de boas-vindas e introdução ao FURIA Bot  
- `/loja` — Exibe produtos disponíveis na loja oficial da FURIA  
- `/proximosjogos` — Mostra os próximos jogos do time de CS2  
- `/resultados` — Exibe os resultados dos últimos 5 jogos no CS2  
- `/torcida` — Inicia o simulador de conversa da torcida  
- `/lineup` — Lista os jogadores e a comissão técnica  
- `/titulos` — Mostra os títulos conquistados pela FURIA no CS2  
- `/ativarnotificacao` — Ativa notificações automáticas de novos jogos  
- `/desativarnotificacao` — Cancela as notificações de jogos

---

## 🚀 Como Rodar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/icaropereira1/FURIA-Bot
cd FURIA-Bot
```

### 2. Criar contas e obter chaves de API

- **Telegram Bot**: Crie um bot e gere sua chave via [BotFather](https://telegram.me/BotFather)  
- **PandaScore**: Cadastre-se e obtenha sua chave de API em [pandascore.co](https://www.pandascore.co)

### 3. Configurar variáveis de ambiente

Entre no arquivo `.env` e modifique seguinte conteúdo:

```env
TELEGRAM_API_KEY=sua_chave_telegram_aqui
PANDASCORE_API_KEY=sua_chave_pandascore_aqui
```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar o bot

```bash
python -m bot.main
```

---

## 📁 Estrutura do Projeto

```
FURIA-Bot/
├── bot/
│   ├── cache/
│   ├── core/
│   ├── handlers/
│   ├── services/
│   ├── main.py
│   └── __init__.py
├── chat_notificacao/
├── requirements.txt
├── README.md
└── .env
```

---

## 🛠️ Exemplo de Uso

**Usuário**: `/proximosjogos`  
**Bot**: 🔥 Próximos jogos da FURIA: 🔥

🏆 Campeonato: Astana 2025  
🆚 TheMongolz  
📅 10/05/2025 às 05:00  
🔴 Assistir ao vivo: [https://www.twitch.tv/PGL](https://www.twitch.tv/PGL)

---

## 📌 Próximos Passos

- [ ] Implementar bate-papo com IA  
- [ ] Adicionar estatísticas pagas dos jogadores via PandaScore  
- [ ] Adicionar histórico de mensagens no modo bate-papo  
- [ ] Criar painel administrativo web para notificações  
- [ ] Expandir para outras modalidades (Valorant, R6, Rocket League)  
- [ ] Suporte a múltiplos idiomas  

---

## 🧪 Testes

Testes automatizados serão adicionados em versões futuras.

---

## 🤝 Contribuindo

Pull requests são bem-vindos! Para grandes mudanças, abra uma issue antes.

---

## ✒️ Autor

Desenvolvido por **Ícaro Pereira Alves**  
Estudante de Engenharia de Computação — UFG  
📧 Email: [xicaroestudos@gmail.com](mailto:xicaroestudos@gmail.com)  
🐙 GitHub: [@icaropereira1](https://github.com/icaropereira1)

---

## 🖤 FURIA

> "Somos uma família. Somos FURIA."
