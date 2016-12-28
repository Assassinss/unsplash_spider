from . import bucket, photo_bucket


def list():

    prefix = None

    limit = 24

    delimiter = None

    marker = None

    ret, eof, info = bucket.list(photo_bucket, prefix, marker, limit, delimiter)

    print('List status: ', info.status_code)

    if ret:
        return ret.get('items')
    else:
        return None


def delete():
    items = list()

    if items:
        for item in items:
            ret, info = bucket.delete(photo_bucket, item['key'])
            if 200 <= info.status_code < 300:
                print('Delete successfully')
            else:
                print('Delete failure')

