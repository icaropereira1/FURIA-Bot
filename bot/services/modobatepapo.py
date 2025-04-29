import openai

openai.api_key = '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'


def get_resposta_ia(mensagem):
    try:
        resposta = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um chatbot da organização FURIA Esports. "
                        "Responda apenas perguntas sobre a FURIA ou sobre o jogo CS2, sempre em português do Brasil. "
                        "Se a pergunta não for relacionada, diga que só pode responder perguntas sobre FURIA ou CS2."
                    )
                },
                {
                    "role": "user",
                    "content": mensagem
                }
            ]
        )

        return resposta.choices[0].message['content'].strip()

    except Exception as e:
        return "⚠️ Ocorreu um erro ao tentar gerar a resposta com a IA. Tente novamente mais tarde."