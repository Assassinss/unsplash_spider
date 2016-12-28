from . import bucket, bucket_name


def fetch_photo(url):

    key = '{key}.{mimeType}'.format(key=url[27: 38], mimeType='jpg')

    ret, info = bucket.fetch(url=url, bucket=bucket_name, key=key)

    print("ret: ", ret)
    print("info: ", info)
    if 200 <= info.status_code < 300:
        print("Upload successfully")
    elif info.status_code == -1:
        print("Upload failure")
