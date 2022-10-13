import requests
def unistream_price():
    headers = {
        'origin': 'https://unistream.ru',
        # 'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'ru',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 YaBrowser/17.1.0.2034 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://unistream.ru/?utm_source=yandex.ru&utm_medium=organic&utm_campaign=yandex.ru&utm_referrer=yandex.ru',
        'authority': 'online.unistream.ru',
    }

    params = {
        'destination': 'UZB',
        'amount': '1000',
        'currency': 'UZS',
        'accepted_currency': 'RUB',
        'profile': 'unistream_front',
    }

    response = requests.get('https://online.unistream.ru/card2cash/calculate', params=params, headers=headers)
    x = response.text
    x = x.split(',')
    x = x[-3]
    price = x.split(':')
    price = price[1].split('.')
    if len(price[1]) >= 4:
        q = price[1][:3]
        a = price[0] + '.' + q
        return a
    new_price = price[1][:3]
    price = price[0]+'.'+new_price
    return price




