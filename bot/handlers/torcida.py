from bot.core.bot_instance import bot
import random

def register(bot):
    @bot.message_handler(commands=['torcida'])
    def simulador_torcida(message):
        chat_id = message.chat.id
        user_first_name = message.from_user.first_name or "Torcedor"

        jogadores = ["KSCERATO", "yuurih", "molodoy", "YEKINDAR", "fallen"]
        emojis = ["🔥", "💥", "🐆", "🎯", "🏆", "📢", "🎉", "💣", "🚀"]

        gritos_normais = [
            f"{random.choice(emojis)} VAMO FURIA! FURIA! FURIA!",
            f"{random.choice(emojis)} {random.choice(jogadores)} tá jogando o fino!",
            f"{random.choice(emojis)} É agora! Bora, FURIA!",
            f"{random.choice(emojis)} AQUI É FURIA, NÃO É PASSEIO!",
        ]

        gritos_explosivos = [
            f"{random.choice(emojis)}{" FURIA!".join([''] * random.randint(4, 7))}",
            f"{random.choice(emojis)} FURIAAAAAAAAAAAAAAAAAA!!! {random.choice(emojis)}",
            f"{random.choice(jogadores).upper()} INSANO! QUE BALAAAAAAAA! 💥💥💥",
            f"{user_first_name.upper()} TÁ MALUCO COM ESSA FURIA! 🐆🔥",
        ]

        gritos_zoeiros = [
            "TÁ COM MEDO, JOGA O MOUSE FORA! 😂",
            "BALA, TÁTICA E TRADIÇÃO! É A FURIA!",
            f"O ADVERSÁRIO JÁ PEDIU PAUSA TÉCNICA! 🧠💣",
            f"FURIA VAI ENVIAR CURRÍCULO PROS CARA... PQ TÁ DANDO AULA! 📚🔥",
        ]

        gritos_motivacionais = [
            "JOGA COM O CORAÇÃO, FURIA! ❤️‍🔥",
            "AQUI É BRASIL, É FURIA, É RAÇA!",
            "SOMOS MILHÕES TORCENDO JUNTO! 🇧🇷🔥",
            f"COM FÉ, FOCO E {random.choice(jogadores).upper()}, VEM O TÍTULO! 🏆",
        ]

        categoria = random.choices(
            ["normal", "explosivo", "zoeiro", "motivacional"],
            weights=[50, 20, 15, 15],  # probabilidade
            k=1
        )[0]

        if categoria == "normal":
            grito = random.choice(gritos_normais)
        elif categoria == "explosivo":
            grito = random.choice(gritos_explosivos)
        elif categoria == "zoeiro":
            grito = random.choice(gritos_zoeiros)
        else:
            grito = random.choice(gritos_motivacionais)

        bot.send_message(chat_id, grito)


