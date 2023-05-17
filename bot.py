import telebot
import requests
import json

CHAVE_API = ''
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=['opcao1'])
def responder(mensagem):

    requisicao= requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-BRL')
    moedas = requisicao.json()

    usd = float(moedas["USDBRL"]["bid"])
    btc = float(moedas["BTCBRL"]["bid"])
    eth = float(moedas["ETHBRL"]["bid"])
    bot.send_message(mensagem.chat.id, f'Cotações de Hoje:\n\n Dolar: R${usd:,.2f}\n Biticoin: R${btc:,.2f}\n Ethereum: R${eth:,.2f}')

@bot.message_handler(commands=['opcao2'])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado pelo abraço! Tenha um ótimo dia.")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar(Clique em uma Opção):
/opcao1 Ver cotação do BTC,USD,ETH
/opcao2 Mandar um  Abraço pro isael
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)



bot.polling()