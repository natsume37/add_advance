import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
# 需要node环境！！！
# 如果执行if分支，则需注意导入包的顺序，这样才能进行定义编码，可能不会报错
# 如果执行else分支，则只需要导入import subprocess即可

def decrypt_data(msg, select=True):
    if select:
        js_code = '''
                    const crypto = require('crypto');
                    var o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
                    var n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
                    function decrypt_data(t) {
                        const a = crypto.createHash('md5').update(o).digest()
                            , r = crypto.createHash('md5').update(n).digest()
                            , i = crypto.createDecipheriv("aes-128-cbc", a, r);
                        let s = i.update(t, "base64", "utf-8");
                        return s += i.final("utf-8"),
                        s
                    }
                  '''
        return execjs.compile(js_code).call('decrypt_data', msg)
    else:
        return subprocess.Popen(['node', './js实现.js', msg], stdout=subprocess.PIPE).stdout.read()
if __name__ == '__main__':
    msg = 'Z21kD9ZK1ke6ugku2ccWuwRmpItPkRr5XcmzOgAKD0GcaHTZL9kyNKkN2aYY6yiOmuh9nNfHAP8nmQ1U8cWs8AsPk-qsI0Oi3S_EIBseAYim7wIT81haR5hYOoRK649xgJV2OCWi8mdYBjL3nNw_m22LYYPt_dDmdoFiMiMwddUtdr42g1o9A-MqBEvxSK-H'
    print(decrypt_data(msg))