'''Получаем данные с Garantex'''
import requests

def price_garantex():
    #открываем текстовый файл, получаем токен
    with open('JWT.txt') as f:
        text_jwt = f.read()
    JWT = text_jwt
    host = 'garantex.io'
    #делаем запрос
    ret = requests.get('https://garantex.io/api/v2/depth',
                       data = {'market':'usdtrub'})
    #получаем данные с запроса и берем первую цену
    response = ret.json()
    text2 = response['bids']
    bids = text2[0]
    bids = bids['price']
    text = response['asks']
    x = text[0]
    price = x['price']
    #Возращаем в формате str
    return price, bids
#63.8






