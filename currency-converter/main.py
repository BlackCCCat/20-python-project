import json
import datetime
import os
from currency import Currency
from api import ApiInfo



class UpdateCurrency():
    def __init__(self) -> None:
        self.currency_file = 'currency.json'
    
    def is_api_empty(self):
        # 检查API是否存在
        api = ApiInfo.API
        if api:
            return False
        else:
            return True

    def is_content_empty(self):
        # 检查汇率文件是否为空，是的话返回True
        with open(self.currency_file) as f:
            res = f.read()
            if res:
                return False if 'data' in res else True
            else:
                return True
    
    def check(self, interval=6):
        """
        :params: interval: 每隔多少小时更新汇率信息
        """
        result = None
        # API和汇率内容都为空，提示申请API
        if self.is_api_empty() and self.is_content_empty():
            print('请先在 https://app.currencyapi.com/ 申请免费API使用')
            return
        
        # 文件不存在，且API为空，提示申请API
        if not os.path.exists(self.currency_file) and self.is_api_empty():
            print('请先在 https://app.currencyapi.com/ 申请免费API使用')
            return

        # 文件不存在，但API不为空
        if not os.path.exists(self.currency_file) and not self.is_api_empty():
            result = Currency.get_api_info()
        
        # 文件存在
        if os.path.exists(self.currency_file):
            # 如果文件内容为空
            if self.is_content_empty():
                # API为空，提示申请API
                if self.is_api_empty():
                    print('请先在 https://app.currencyapi.com/ 申请免费API使用')
                    return
                
                result = Currency.get_api_info()

            else:#如果文件不为空，那么进行更新时间的比较
                # 获取当前时间的datetime格式
                current_time = datetime.datetime.now()
                # 获取汇率文件最后修改时间的时间戳
                exists_currency_time = os.stat(self.currency_file).st_mtime
                # 将时间戳转换为datetime格式
                exists_currency_time = datetime.datetime.fromtimestamp(exists_currency_time)
                
                if current_time.date() != exists_currency_time.date():# 如果日期不一样就更新汇率
                    # API为空，无法更新
                    if self.is_api_empty():
                        print('请先在 https://app.currencyapi.com/ 申请免费API使用')
                        return
                    result = Currency.get_api_info()
                elif current_time.hour - exists_currency_time.hour >= interval:# 如果日期一样相差超过6小时就更新汇率
                    # API为空，无法更新
                    if self.is_api_empty():
                        print('请先在 https://app.currencyapi.com/ 申请免费API使用')
                        return
                    result = Currency.get_api_info()
                else:
                    pass
                
        if result:
            Currency.currency_to_json(data=result)# 获取的汇率写入文件
            
        return True


class CurrencyConverter():
    def __init__(self, update: UpdateCurrency):
        # 检查汇率更新情况
        # self.check_currency = update.is_content_empty()
        # self.currency_file = 'currency.json'
        # if self.check_currency:
        #     check_res = update.check()
        # else:
        #     check_res = True
        # if check_res:
        #     self.currency = self.getAllCurrency()
        #     self.USD = self.getOneCurrency()
        #     self.run()
        self.currency_file = 'currency.json'
        check_res = update.check()
        if check_res:
            self.currency = self.getAllCurrency()
            self.USD = self.getOneCurrency()
            self.run()

        

    def getAllCurrency(self):
        """
        获取所有汇率信息
        """
        with open(self.currency_file, 'r') as f:
            # last_updated_at = json.load(f)['meta']
            currency = json.load(f)['data']
        return currency
    
    def getOneCurrency(self, code='USD'):
        """
        获取指定货币汇率
        """
        _ = self.currency.get(code)
        if _:
            return _.get('value')
        
    
    def run(self):
        amount = float(input('Enter the amount to convert: '))
        source = input('Enter the source currency: ').upper()
        target = input('Enter the target currency: ').upper()

        try:
            if source != self.USD:
                amount_to_usd = amount / self.getOneCurrency(source)
                usd_to_target = round(amount_to_usd * self.getOneCurrency(target), 2)
            else:
                usd_to_target = round(amount * self.getOneCurrency(target), 2)

            print(f'Converted amount: {usd_to_target} {target}')
        except:
            print('Invalid input')
        
        


if __name__ == "__main__":
    UpdateCurrency = UpdateCurrency()
    CurrencyConverter(UpdateCurrency)



        





