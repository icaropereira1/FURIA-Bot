from bot.core.bot_instance import bot
from bot.handlers import ativar_desativar_notificacoes, start, loja, lineup, proximosjogos, titulos, resultados, resultadosdetalhados, torcida
from bot.services.monitoramento import iniciar_monitoramento

iniciar_monitoramento(bot)

# Registra handlers
start.register(bot)
loja.register(bot)
lineup.register(bot)
proximosjogos.register(bot)
titulos.register(bot)
ativar_desativar_notificacoes.register(bot)
resultados.register(bot)
resultadosdetalhados.register(bot)
torcida.register(bot)

print("Bot iniciado...")
bot.polling()