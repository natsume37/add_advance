# coding : utf-8
# 夏目&青一
# @name:豆瓣评分
# @time: 2023/6/6  15:57
# 简略版

import time

import requests
from bs4 import BeautifulSoup


def every_page(url):
    res = requests.get(url, headers=header)
    html = BeautifulSoup(res.text, "html.parser")
    response = html.select('#content > div > div.article > ol li')
    for item in response:
        linl = item.select('li > div > div.info > div.hd > a')
        for i in linl:
            link = i['href']
            name = i.select('a > span')[0].text

        score = item.select('li > div > div.info > div.bd > div > span.rating_num')[0].text
        print(f"link:{link}  name:{name}  score:{score}")


if __name__ == '__main__':
    url_list = 'https://movie.douban.com/top250?start={}&filter='
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    for i in range(10):
        url = url_list.format(i * 25)
        every_page(url)
    every_page('https://movie.douban.com/top250?start=25&filter=')
