import configurations
from configurations import KEY, APIURL, APIKEY

import requests, json


class ConverterError(Exception):
    pass


class CurrencyConverter():

    @staticmethod
    def convert(base: str, quote: str, amount: str):
        if base == quote:
            raise ConverterError(f'Невозможно конвертировать {base} in {quote}')

        try:
            base_ticker = KEY[base]
        except KeyError:
            raise ConverterError(f'Не удалось обработать валюту! {base}')

        try:
            quote_ticker = KEY[quote]
        except KeyError:
            raise ConverterError(f'Не удалось обработать валюту! {quote}')

        try:
            amount = float(amount)
        except KeyError:
            raise ConverterError(f'Не удалось обработать {amount}')

        r = requests.get(f'{APIURL}{base_ticker}{quote_ticker}&key={APIKEY}')
        total_base = float(json.loads(r.content)['data'][KEY[base] + KEY[quote]]) * amount
        return total_base

