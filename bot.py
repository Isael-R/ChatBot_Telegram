import telebot
from chaveApi import chave_api_telgram, chave_api_alpha
import requests
import json



CHAVE_API = chave_api_telgram
bot = telebot.TeleBot(CHAVE_API)

#Opção 1 gera o preço atual do USD, BTC, ETH
@bot.message_handler(commands=['opcao1'])
def responder(mensagem):

    requisicao= requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL,ETH-BRL')
    moedas = requisicao.json()

    usd = float(moedas["USDBRL"]["bid"])
    btc = float(moedas["BTCBRL"]["bid"])
    eth = float(moedas["ETHBRL"]["bid"])
    bot.send_message(mensagem.chat.id, f'Cotações de Hoje:\n Dolar: R${usd:,.2f}\n Biticoin: R${btc:,.2f}\n Ethereum: R${eth:,.2f}')

#Opção 2 Manda um Abraço para o Bot
@bot.message_handler(commands=['opcao2'])
def responder(mensagem):
    bot.send_message(mensagem.chat.id, "Obrigado pelo abraço! Tenha um ótimo dia.")

#Opção 3 Mostra cotação diaria do mxrf11
@bot.message_handler(commands=['opcao3'])
def responder(mensagem):
    mxrf_request = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=MXRF11.SA&apikey={chave_api_alpha}')
    cota_mxrf = mxrf_request.json()
    mxrf11 = [cota_mxrf['Global Quote']['07. latest trading day'],cota_mxrf['Global Quote']['02. open'], cota_mxrf['Global Quote']['03. high'], cota_mxrf['Global Quote']['08. previous close']]
 
    bot.send_message(mensagem.chat.id, f""" 
    -------- MXRF11 {mxrf11[0]} --------\n
    Abertura: R${float(mxrf11[1]):,.2f}
    Max: R${float(mxrf11[2]):,.2f}
    Fechamento: R${float(mxrf11[1]):,.2f}
        """)


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Escolha uma opção para continuar(Clique em uma Opção):\n
/opcao1 Ver cotação do BTC,USD,ETH\n
/opcao2 Mandar um  Abraço pro isael\n
/opcao3 Ver cotação do fundo imobiliário MXRF11\n 
Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""
    bot.reply_to(mensagem, texto)


bot.polling()