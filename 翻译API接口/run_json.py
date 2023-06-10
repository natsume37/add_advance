import requests, hashlib, time, random, json
from js实现 import decrypt_data


class YouDaoFanYi:
    def __init__(self, content):
        self.content = content
        self.session = requests.Session()
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "https://fanyi.youdao.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        self.get_cookies()

    def get_cookies(self):
        try:
            _ = 2147483647 * random.random()
            cookies = {
                "OUTFOX_SEARCH_USER_ID_NCOO": str(_),
            }
            response = requests.get(f"https://rlogs.youdao.com/rlog.php?_npid=fanyiweb&_ncat=event"
                                    f"&_ncoo={_}&_ntms={str(int(time.time() * 1000))}"
                                    f"&show=text_translation_result", headers=self.headers, cookies=cookies)
            self.cookies = {
                "search-popup-show": "9-7",
                "OUTFOX_SEARCH_USER_ID_NCOO": str(_),
                "OUTFOX_SEARCH_USER_ID": response.cookies.values()[0]
            }
        except Exception as e:
            raise Exception("cookies获取失败！！！程序退出>>>异常信息：", e)

    def get_sign(self):
        msg = f'client=fanyideskweb&mysticTime={self.timestamp}&product=webfanyi&key=fsdsogkndfokasodnaso'
        return hashlib.md5(msg.encode('utf-8')).hexdigest()

    def get_data(self):
        self.timestamp = str(int(time.time() * 1000))
        data = {
            "i": self.content,
            "from": "auto",
            "to": "",
            "domain": "0",
            "dictResult": "true",
            "keyid": "webfanyi",
            "sign": self.get_sign(),
            "client": "fanyideskweb",
            "product": "webfanyi",
            "appVersion": "1.0.0",
            "vendor": "web",
            "pointParam": "client,mysticTime,product",
            "mysticTime": self.timestamp,
            "keyfrom": "fanyi.web"
        }
        text = self.session.post("https://dict.youdao.com/webtranslate", headers=self.headers,
                                 cookies=self.cookies, data=data).text
        # 直接转JSON
        self.res_data = json.loads(decrypt_data(text))
        print(type(self.res_data))

    def parse_data(self):
        res = self.res_data
        return res

    def main(self):
        try:
            # self.content = input("输入要翻译的文本(0退出)：").strip()
            if self.content == '0': return ""
            self.get_data()
            res = self.parse_data()
            self.session.close()
            return res
        except:
            self.session.close()


if __name__ == '__main__':
    res = YouDaoFanYi("你好").main()
    print(res)
