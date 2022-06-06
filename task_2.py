import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',

            'Authorization': f'OAuth {token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self._get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self):
        print(os.listdir())
        filename = input('Скопируйте имя файла и вставьте сюда -> : ')
        disk_file_path = input('Введите путь загрузки: ')
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Получилось')


if __name__ == '__main__':
    ya = YaUploader(token)
    ya.upload()
