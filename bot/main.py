from bot.core.bot_instance import bot
from bot.handlers import start, loja, lineup, proximosjogos, titulos, batepapo, ativar_des_notificações, resultados
from bot.services.monitoramento import iniciar_monitoramento

iniciar_monitoramento(bot)

# Registra handlers
start.register(bot)
loja.register(bot)
lineup.register(bot)
proximosjogos.register(bot)
titulos.register(bot)
ativar_des_notificações.register(bot)
resultados.register(bot)

print("Bot iniciado...")
bot.polling()