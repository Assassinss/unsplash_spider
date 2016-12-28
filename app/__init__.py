import json
from qiniu import Auth, BucketManager


def getkey(path):
    with open(path, 'r') as fp:
        keys = json.load(fp, encoding='UTF-8')
        return keys['access_key'], keys['secret_key']


auth = Auth(*getkey('app/key.json'))
bucket = BucketManager(auth)

bucket_name = 'photo'
