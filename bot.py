import telebot

CHAVE_API = ''
bot = telebot.TeleBot(CHAVE_API)

def verificar(messagem):
    return True

@bot.message_handler(func=verificar)
def responder(messagem):
    bot.reply_to(messagem, 'Olá aqui é o Bot do Isael')



bot.polling()