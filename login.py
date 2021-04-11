import time
import requests
from urllib.parse import urlencode
from hashlib import md5
import qrcode


APPKEY = "4409e2ce8ffd12b8"
APPSEC = "59b43e04ad6965f34319062b478f83dd"


def get_sign(params):
    items = sorted(params.items())
    return md5(f"{urlencode(items)}{APPSEC}".encode('utf-8')).hexdigest()


def qr_login():
    params = {
        'appkey': APPKEY,
        'local_id': 0,
        'ts': int(time.time())
    }
    params['sign'] = get_sign(params)
    url = f"http://passport.bilibili.com/x/passport-tv-login/qrcode/auth_code"
    r = requests.post(url, params=params)
    print(r.text)
    qr = qrcode.QRCode()
    qr.add_data(r.json()['data']['url'])
    img = qr.make_image()
    img.show()

    params = {
        'appkey': APPKEY,
        'local_id': 0,
        'ts': int(time.time())
    }
    params['auth_code'] = r.json()['data']['auth_code']
    params['sign'] = get_sign(params)
    url = f"http://passport.bilibili.com/x/passport-tv-login/qrcode/poll"
    while True:
        r = requests.post(url, params=params)
        print(r.text)
        if r.json()['code'] == 0:
            break
        time.sleep(1)

if __name__ == "__main__":
    qr_login()