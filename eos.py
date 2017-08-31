#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import decimal
import hashlib
import json
import time
import requests
from datetime import datetime, timezone, timedelta

def main():
    while True:
        try:
            resp = requests.get(url='http://eos.io/eos-sales-statistic.php', timeout=10)
            result = json.loads(resp.text)


            period = 54
            today_sale = result[period]
            today_ico_eth = round(today_sale['dailyTotal'], 2)

            today_ico_end_utc_str = today_sale['ends']

            today_ico_end_utc = datetime.strptime(today_ico_end_utc_str, '%Y-%m-%dT%H:%M:%S.000Z')

            tz_utc_8 = timezone(timedelta(hours=8))
            today_ico_end_bj = today_ico_end_utc.replace(tzinfo=tz_utc_8)
            print(today_ico_end_bj)

            # t = parser.parse(today_ico_end)
            # print(t)

            resp = requests.get(url='https://yunbi.com//api/v2/tickers/ethcny.json', timeout=10)
            result = json.loads(resp.text)

            eth_price = float(result['ticker']['last'])

            eos_sale_price = round(eth_price*today_ico_eth/2000000,2)

            eos_per_eth = round(2000000/today_ico_eth,2)

            resp = requests.get(url='https://yunbi.com//api/v2/tickers/eoscny.json', timeout=10)
            result = json.loads(resp.text)

            eos_price = round(float(result['ticker']['last']),2)

            now = datetime.now() # 获取当前datetime
            print(now)
            # print("投入ETH:%s ETH兑EOS:%s  EOS价格:%s EOS云币价格:%s" % (today_ico_eth, eos_per_eth, eos_sale_price, eos_price))
            print("hedge:today_ico_eth, eos_per_eth, eos_sale_price, eos_yunbi_price:", today_ico_eth, eos_per_eth, eos_sale_price, eos_price)
            # print 'main running'
        except Exception as identifier:
            print(identifier)

        time.sleep(1)


if __name__ == '__main__':
    main()
