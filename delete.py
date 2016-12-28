from qiniu import Auth, BucketManager
import json


def getkey(path):
    with open(path, 'r') as fp:
        keys = json.load(fp, encoding='UTF-8')
        return keys['access_key'], keys['secret_key']


bucket_name = 'photo'
q = Auth(*getkey('key.json'))
bucket = BucketManager(q)


def list():

    prefix = None

    limit = 24

    delimiter = None

    marker = None

    ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)

    print('List status: ', info.status_code)

    if ret:
        return ret.get('items')
    else:
        return None


def delete():
    items = list()

    if items:
        for item in items:
            ret, info = bucket.delete(bucket_name, item['key'])
            if 200 <= info.status_code < 300:
                print('Delete successfully')
            else:
                print('Delete failure')

