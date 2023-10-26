#!/usr/bin/env python3
import requests
from api import ApiInfo

class Currency():
    @staticmethod
    def get_api_info():
        print('获取最新汇率...')
        url = 'https://api.currencyapi.com/v3/latest'
        params = {
                "apikey": ApiInfo.API,
            }
        try:
            _ = requests.get(url=url, params=params).content
            result = _.decode('utf-8')
            return result
        except:
            print('获取最新汇率失败')

        

    @staticmethod
    def currency_to_json(file_name='currency.json', data={}):
        with open(file_name, 'w') as f:
            f.write(data)


def main():
    currency = Currency.get_api_info()
    Currency.currency_to_json(data=currency)


if __name__ == "__main__":
    main()