import requests
from bs4 import BeautifulSoup
from app.delete import delete

from app.upload import fetch_photo


class Unsplash(object):

    host = 'https://unsplash.com/new'

    def fetch_photo_url(self):
        req = requests.get(self.host)
        soup = BeautifulSoup(req.text, "html5lib")
        a_tags = soup.find_all(title='Download photo')
        for tag in a_tags:
            print('photo href : ', tag.attrs['href'])
            self.upload(tag.attrs['href'])

    @staticmethod
    def upload(url):
        fetch_photo(url)


if __name__ == '__main__':
    unsplash = Unsplash()

    delete()

    unsplash.fetch_photo_url()

