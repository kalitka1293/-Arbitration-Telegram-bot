
"""Отправляем запрос, получаем данные с сайта, достаем курс конвентации и возращаем число float 
           'user-agent' - можно доработать заранее в список добавить 'user-agent', и от туда вытаскивать рандомно.
            защита от блокировки          """

def price_koronaPay():
    import requests

    cookies = {
        '_gcl_au': '1.1.563960030.1660506321',
        '_gid': 'GA1.2.1982871326.1660506322',
        '_ym_uid': '1660506322557856576',
        '_ym_d': '1660506322',
        '_dc_gtm_UA-100141486-1': '1',
        '_dc_gtm_UA-100141486-26': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        'tmr_lvid': '37f888f9bb7cb55772502bcdc5e96318',
        'tmr_lvidTS': '1660506321819',
        'qpay-web/3.0_locale': 'ru',
        '_dc_gtm_UA-100141486-2': '1',
        '_dc_gtm_UA-100141486-25': '1',
        '_ga_H68H5PL1N6': 'GS1.1.1660506321.1.1.1660506339.42',
        '_ga': 'GA1.2.70515446.1660506322',
        'tmr_detect': '0%7C1660506342091',
        'tmr_reqNum': '12',
        'ROUTEID': '95d5465b93cbc125|YvlP6',
        '_gali': 'changeable-field-input-amount',
        'qpay-web/3.0_csrf-token-v2': '84f19455da63604929bd25813972356e',
    }

    headers = {
        'authority': 'koronapay.com',
        'accept': 'application/vnd.cft-data.v2.86+json',
        'accept-language': 'ru',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gcl_au=1.1.563960030.1660506321; _gid=GA1.2.1982871326.1660506322; _ym_uid=1660506322557856576; _ym_d=1660506322; _dc_gtm_UA-100141486-1=1; _dc_gtm_UA-100141486-26=1; _ym_isad=2; _ym_visorc=w; tmr_lvid=37f888f9bb7cb55772502bcdc5e96318; tmr_lvidTS=1660506321819; qpay-web/3.0_locale=ru; _dc_gtm_UA-100141486-2=1; _dc_gtm_UA-100141486-25=1; _ga_H68H5PL1N6=GS1.1.1660506321.1.1.1660506339.42; _ga=GA1.2.70515446.1660506322; tmr_detect=0%7C1660506342091; tmr_reqNum=12; ROUTEID=95d5465b93cbc125|YvlP6; _gali=changeable-field-input-amount; qpay-web/3.0_csrf-token-v2=84f19455da63604929bd25813972356e',
        'referer': 'https://koronapay.com/transfers/online/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-application': 'Qpay-Web/3.0',
        'x-csrf-token': '84f19455da63604929bd25813972356e',
    }

    params = {
        'sendingCountryId': 'RUS',
        'sendingCurrencyId': '810',
        'receivingCountryId': 'UZB',
        'receivingCurrencyId': '840',
        'paymentMethod': 'debitCard',
        'receivingAmount': '100',
        'receivingMethod': 'cash',
        'paidNotificationEnabled': 'false',
    }

    response = requests.get('https://koronapay.com/transfers/online/api/transfers/tariffs', params=params,
                            cookies=cookies, headers=headers)
    #Достаем курс из ответа
    x = response.text.replace('[', '')
    x = x.replace(']', '')
    x = x.split(',')
    x = x[-5].split(':')
    #Возращаем в формате str
    return x[1]
#62.92
