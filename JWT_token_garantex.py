"""Получаем  JWT токен
Каждый раз не обязательно создовать новый токен
"""
import random
import time
import requests
import jwt
import datetime
import base64
#Данные (private_key, uid, host) можно найти в личном аккаунте на сайте

def token():
    #открываем текстовый документ и достаем от туда приватный ключ и передаем переменной key
    with open('private_key.txt') as f:
        key = str(f.read())

    with open('uid.txt') as f:
        uid_api = str(f.read())

    private_key = '{'+key+'}'
    print(private_key)

    uid = '{'+uid_api+'}'
    print(uid_api)

    host = 'garantex.io'
    key = base64.b64decode(private_key)
    iat = int(time.mktime(datetime.datetime.now().timetuple()))
    claims = {
    'exp': iat + 1*60*60,
    'jti': hex(random.getrandbits(12)).upper()
    }
    jwt_token = jwt.encode(claims, key, algorithm='RS256')
    print('JWT token requrst %s' %jwt_token)
    ret = requests.post('https://dauth.'+host+ '/api/v1/sessions/generate_jwt', json={'kid':uid, 'jwt_tiken':jwt_token})

    print("JWT response code: %d" % ret.status_code)
    print("JWY response text: %s\n" % ret.text)

    token = ret.json().get('token')

    print("JWT token: %s\n" % token)

    #Записыввает новый токен в текстовый файл, удаляет старый
    with open('JWT.txt', 'w') as f:
        f.write(token)


if __name__ == '__main__':
    token()