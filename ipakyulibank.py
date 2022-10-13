import requests
#https://ru.ipakyulibank.uz/physical/obmen-valyut/kursy

"""Делаем запрос на сайт, получаем данные, обрабатываем и возращаем цену"""

#Функция возращает срез из текста
def between_markers(text, begin, end):
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]


def price_ipakyulibank():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Origin': 'https://ru.ipakyulibank.uz',
        'Referer': 'https://ru.ipakyulibank.uz/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-AppKey': 'blablakey',
        'X-AppLang': 'ru',
        'X-AppRef': '/physical/obmen-valyut/kursy',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.post('https://ipakyulibank.uz:8888/webapi/default/get-other-contents', headers=headers)

    text = response.text
    #Маркеры для функции(от, до)
    stop = '"atm":'
    start = '"office":{"buy":'
    #Получаем срез
    text_price = between_markers(text, start, stop)
    #из полученного текста достаем цену
    new = text_price.split('"')
    #Возращаем в формате str
    return new[1]

#10840 <class 'str'>
