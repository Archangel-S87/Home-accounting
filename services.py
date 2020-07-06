import requests
from requests.exceptions import HTTPError


class Services:

    window = None

    def __init__(self, window):
        self.window = window
        pass

    @staticmethod
    def get(self, url):
        try:
            response = requests.get(url)
            # если ответ успешен, исключения задействованы не будут
            response.raise_for_status()
        except HTTPError as http_err:
            # Сделать вывод в статус
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')

        return ''

