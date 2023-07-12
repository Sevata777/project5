# Домашнее задание «Работа с библиотекой requests, http запросы»
# Таюрский Сергей, FPY-82
# Задание 1

import requests
import operator
response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
names_of_characters = ['Hulk', 'Captain America', 'Thanos']
intelligence = {}
for character in response.json():
    if character['name'] in names_of_characters:
        intelligence[character['powerstats']['intelligence']] = character['name']
intelligence_super_man = max(intelligence.items(), key=operator.itemgetter(1))
print(f'Самый умный супергерой {intelligence_super_man[1]}, с интелектом: {intelligence_super_man[0]}')

# Задание 2

import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
        params = {'path': path, 'overwrite': True}
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        response = requests.get(url, headers=headers, params=params)

        url_upload = response.json().get('href', '')
        with open(path, 'rb') as file:
            response2 = requests.put(url_upload, files={'file':file})
            if 200 <= response2.status_code <= 300:
                print(f'Файл {path} скачен')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = 'Введите Токен'
    uploader = YaUploader(token)
    result = uploader.upload('Введите путь к файлу')

