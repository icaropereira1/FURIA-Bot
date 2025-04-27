import telebot
from telebot import types

def register(bot):
    @bot.message_handler(commands=['loja'])
    def handle_loja(msg):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botao1 = types.KeyboardButton("👕 Vestuário")
        botao2 = types.KeyboardButton("🎒 Acessórios")
        markup.add(botao1, botao2)

        bot.send_message(
            msg.chat.id,
            "Certo, na Loja da Pantera temos Vestuário e Acessórios.\nMe diz aí, o que você quer comprar?",
            reply_markup=markup
        )

    @bot.message_handler(func=lambda message: message.text in ["👕 Vestuário", "🎒 Acessórios"])
    def handle_categoria(msg):
        if msg.text == "👕 Vestuário":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(
                types.KeyboardButton("👕 Camisetas"),
                types.KeyboardButton("🧥 Jaquetas"),
                types.KeyboardButton("👖 Calças"),
                types.KeyboardButton("🩳 Shorts"),
                types.KeyboardButton("👘 Moletons"),
                types.KeyboardButton("👚 Croppeds")
            )
            bot.send_message(
                msg.chat.id,
                "Escolha uma categoria de vestuário 👇",
                reply_markup=markup
            )

        elif msg.text == "🎒 Acessórios":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(
                types.KeyboardButton("🧢 Bonés"),
                types.KeyboardButton("🧦 Meias"),
                types.KeyboardButton("🎒 Mochilas"),
                types.KeyboardButton("👒 Buckets")
            )
            bot.send_message(
                msg.chat.id,
                "Escolha uma categoria de acessórios 👇",
                reply_markup=markup
            )

    @bot.message_handler(func=lambda message: message.text in [
        "🧢 Bonés", "🧦 Meias", "🎒 Mochilas", "👒 Buckets",
        "👕 Camisetas", "🧥 Jaquetas", "👖 Calças", "🩳 Shorts", "👘 Moletons", "👚 Croppeds"
    ])
    def handle_produtos(msg):
        links = {
            "🧢 Bonés": "https://www.furia.gg/produtos/acessorios/bones",
            "🧦 Meias": "https://www.furia.gg/produtos/acessorios/meias",
            "🎒 Mochilas": "https://www.furia.gg/produtos/acessorios/mochilas",
            "👒 Buckets": "https://www.furia.gg/produtos/acessorios/buckets",
            "👕 Camisetas": "https://www.furia.gg/produtos/vestuario/camisetas",
            "🧥 Jaquetas": "https://www.furia.gg/produtos/vestuario/jaquetas",
            "👖 Calças": "https://www.furia.gg/produtos/vestuario/calcas",
            "🩳 Shorts": "https://www.furia.gg/produtos/vestuario/shorts",
            "👘 Moletons": "https://www.furia.gg/produtos/vestuario/moletons",
            "👚 Croppeds": "https://www.furia.gg/produtos/vestuario/croppeds"
        }

        link = links.get(msg.text)
        if link:
            bot.send_message(
                msg.chat.id,
                f"Aqui está! [Clique aqui para ver {msg.text.split(' ')[1]} da FURIA]({link})",
                parse_mode="Markdown"
            )
