import requests
from lxml import html
import time
import logging

log = logging.getLogger('')


def check():
    try:
        url_exchange = "https://yandex.ru"

        result = requests.get(url_exchange)

        test = html.fromstring(result.text)
        result1 = test.xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div/span/span/text()')
        result2 = test.xpath('//*[@id="wd-_topnews"]/div/div[3]/div/div/div/a/text()')
        print(f'{result2[0]}: {result1[0]}\n{result2[1]}: {result1[1]}')
        time.sleep(5)
        check()
    except:
        print('')


if __name__ == '__main__':
    check()
