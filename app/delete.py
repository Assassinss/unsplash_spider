from . import bucket, bucket_name


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

