# -*- coding: utf-8 -*-
import json
from qiniu import Auth, BucketManager


def getkey(path):
    with open(path, 'r') as fp:
        keys = json.load(fp, encoding='UTF-8')
        return keys['access_key'], keys['secret_key']


q = Auth(*getkey('key.json'))
bucket = BucketManager(q)


def fetch_photo(url):

    bucket_name = "photo"

    key = '{key}.{mimeType}'.format(key=url[27: 38], mimeType='jpg')

    ret, info = bucket.fetch(url=url, bucket=bucket_name, key=key)

    print("ret: ", ret)
    print("info: ", info)
    if 200 <= info.status_code < 300:
        print("Upload successfully")
    elif info.status_code == -1:
        print("Upload failure")
