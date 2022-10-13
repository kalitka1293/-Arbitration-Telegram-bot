import requests
def price_binance():
    cookies = {
        'cid': 'gni2H0yv',
        'bnc-uuid': '4fe5b178-6fa5-415c-974c-0a354e1b3507',
        'source': 'organic',
        'campaign': 'www.google.com',
        'sys_mob': 'no',
        '_gcl_au': '1.1.227382009.1659947762',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY': '33d1f4486621acfbb5924463807c54fc46dd05b9',
        'fiat-prefer-currency': 'EUR',
        'videoViewed': 'yes',
        'common_fiat': 'UZS',
        'se_gd': 'ANbBxA1sBFXDxBRFQDQMgZZCRCQgFBTWlNU9bUkN1hdVwGVNXV0X1',
        'se_sd': 'BYNFgBQ8RRbEh1bBTEAxgZZDAXVYKETVVtR9bUkN1hdVwEFNXVUe1',
        'se_gsd': 'dDMnFTBlIjolUBEhIBwiIy0HCg4MBQYVUVpDV1xRVlhbNFNS1',
        'd1og': 'web.493442258.E48DFD8765B3B39E7EE27131034D9519',
        'r2o1': 'web.493442258.6FE6FA8CF02971B1365C79D05BD81A41',
        'f30l': 'web.493442258.0F0EE51E9668E63FBD6B470D8FD4EBD8',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22493442258%22%2C%22first_id%22%3A%221827c98d50143a-02ea05bd6b74a7-26021a51-1327104-1827c98d502444%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%221827c98d50143a-02ea05bd6b74a7-26021a51-1327104-1827c98d502444%22%7D',
        '_gaexp': 'GAX1.2.eUNc73mWR0uGHQECyHs6ew.19305.1',
        'lang': 'ru',
        '_gid': 'GA1.2.2060698251.1660229909',
        'BNC_FV_KEY_EXPIRE': '1660251509979',
        'showBlockMarket': 'false',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Aug+11+2022+18%3A07%3A01+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=16eab7fc-0f1e-4c3c-9587-04ba4076e66f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false',
        '_ga_3WP50LGEEC': 'GS1.1.1660229910.2.1.1660230427.9',
        '_ga': 'GA1.2.1926237063.1659947758',
        '_gat_UA-162512367-1': '1',
    }

    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'bnc-uuid': '4fe5b178-6fa5-415c-974c-0a354e1b3507',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        # Already added when you pass json=
        # 'content-type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'cid=gni2H0yv; bnc-uuid=4fe5b178-6fa5-415c-974c-0a354e1b3507; source=organic; campaign=www.google.com; sys_mob=no; _gcl_au=1.1.227382009.1659947762; userPreferredCurrency=RUB_USD; BNC_FV_KEY=33d1f4486621acfbb5924463807c54fc46dd05b9; fiat-prefer-currency=EUR; videoViewed=yes; common_fiat=UZS; se_gd=ANbBxA1sBFXDxBRFQDQMgZZCRCQgFBTWlNU9bUkN1hdVwGVNXV0X1; se_sd=BYNFgBQ8RRbEh1bBTEAxgZZDAXVYKETVVtR9bUkN1hdVwEFNXVUe1; se_gsd=dDMnFTBlIjolUBEhIBwiIy0HCg4MBQYVUVpDV1xRVlhbNFNS1; d1og=web.493442258.E48DFD8765B3B39E7EE27131034D9519; r2o1=web.493442258.6FE6FA8CF02971B1365C79D05BD81A41; f30l=web.493442258.0F0EE51E9668E63FBD6B470D8FD4EBD8; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22493442258%22%2C%22first_id%22%3A%221827c98d50143a-02ea05bd6b74a7-26021a51-1327104-1827c98d502444%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%221827c98d50143a-02ea05bd6b74a7-26021a51-1327104-1827c98d502444%22%7D; _gaexp=GAX1.2.eUNc73mWR0uGHQECyHs6ew.19305.1; lang=ru; _gid=GA1.2.2060698251.1660229909; BNC_FV_KEY_EXPIRE=1660251509979; showBlockMarket=false; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+11+2022+18%3A07%3A01+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=16eab7fc-0f1e-4c3c-9587-04ba4076e66f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false; _ga_3WP50LGEEC=GS1.1.1660229910.2.1.1660230427.9; _ga=GA1.2.1926237063.1659947758; _gat_UA-162512367-1=1',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6Ijg2NCwxNTM2IiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODI0LDE1MzYiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgMTAiLCJicmFuZF9tb2RlbCI6InVua25vd24iLCJzeXN0ZW1fbGFuZyI6InJ1LVJVIiwidGltZXpvbmUiOiJHTVQrMyIsInRpbWV6b25lT2Zmc2V0IjotMTgwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiI2ZjlkYTJhNiIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChBTUQpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoQU1ELCBBTUQgUmFkZW9uKFRNKSBWZWdhIDggR3JhcGhpY3MgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJFdXJvcGUvTW9zY293IiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwMy4wLjAuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6IjRhZWQ5ZGYyNGY2NGFkNzBjOTVhNzZlNjA5N2IyZDUyIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiIn0=',
        'fvideo-id': '33d1f4486621acfbb5924463807c54fc46dd05b9',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/ru/trade/Humo/USDT?fiat=UZS',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-trace-id': 'e7f1864f-fea2-4105-ae91-6d3f812e9fc2',
        'x-ui-request-trace': 'e7f1864f-fea2-4105-ae91-6d3f812e9fc2',
    }

    json_data = {
        'page': 1,
        'rows': 10,
        'payTypes': [
            'Humo',
        ],
        'countries': [],
        'publisherType': None,
        'fiat': 'UZS',
        'tradeType': 'BUY',
        'asset': 'USDT',
        'merchantCheck': False,
    }

    response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', cookies=cookies, headers=headers, json=json_data)

    x = response.text
    x = x.split(',')
    spis = []
    for i in x:
        if '"price"' in i:
            spis.append(i)
    price = str(spis[2])
    price = price.split(':')
    price = price[1]
    price = price.replace('"', '')
    return price

