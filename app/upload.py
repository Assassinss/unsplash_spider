from . import bucket, photo_bucket

index = 0


def fetch_photo(url):

    global index

    index += 1

    key = '{index}-{key}.{mimeType}'.format(index=index, key=url[27: 38], mimeType='jpg')

    ret, info = bucket.fetch(url=url, bucket=photo_bucket, key=key)

    print("ret: ", ret)
    print("info: ", info)
    if 200 <= info.status_code < 300:
        print("Upload successfully")
    elif info.status_code == -1:
        print("Upload failure")
