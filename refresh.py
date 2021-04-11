import json
import os
from base64 import b64encode
from datetime import datetime
from hashlib import md5
from urllib.parse import urlencode

import requests
from nacl import encoding, public


def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


token = os.environ['REPO_ACCESS_TOKEN']
owner = 'SK-415'
repo = 'BiliSessDataShare'
base_address = f"https://{owner}:{token}@api.github.com/repos/{owner}/{repo}/actions/secrets/"
headers={'accept': 'application/vnd.github.v3+json'}
proxies={'http': None, 'https': None}


def get(route):
    url = base_address + route
    return requests.get(url, proxies=proxies, headers=headers).json()


def put(route, params):
    url = base_address + route
    data = json.dumps(params)
    return requests.put(url, data=data, headers=headers, proxies=proxies).status_code


def get_public_key():
    r = get('public-key')
    return r['key_id'], r['key']


def update_secret(name, value):
    encrypt_value = encrypt(KEY, value)
    params = {
        'encrypted_value': encrypt_value,
        'key_id': KEY_ID
    }
    return put(name, params)

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
APPKEY = "4409e2ce8ffd12b8"
APPSEC = "59b43e04ad6965f34319062b478f83dd"

def get_sign(params):
    items = sorted(params.items())
    return md5(f"{urlencode(items)}{APPSEC}".encode('utf-8')).hexdigest()

def refresh():
    params = {
        'access_token': ACCESS_TOKEN,
        'appkey': APPKEY,
        'refresh_token': REFRESH_TOKEN
    }
    params['sign'] = get_sign(params)
    url = f"https://passport.bilibili.com/api/v2/oauth2/refresh_token"
    r = requests.post(url, params=params).json()['data']
    access_token = r['token_info']['access_token']
    refresh_token = r['token_info']['refresh_token']
    sessdata = r['cookie_info']['cookies'][4]['value']
    update_secret('access_token', access_token)
    update_secret('refresh_token', refresh_token)
    with open('SESSDATA', 'w', encoding='utf-8') as f:
        f.write(json.dumps({'value': sessdata, 'updated': str(datetime.now())}))


if __name__ == "__main__":
    KEY_ID, KEY = get_public_key()
    refresh()
