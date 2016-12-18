from bs4 import BeautifulSoup
import requests


class Unsplash(object):

    host = 'https://unsplash.com/'

    def fetch_photo_url(self):
        req = requests.get(self.host)
        soup = BeautifulSoup(req.text, "html5lib")
        a_tags = soup.find_all(title='Download photo')
        for tag in a_tags:
            print('photo href : ', tag.attrs['href'])


if __name__ == '__main__':
    unsplash = Unsplash()

    unsplash.fetch_photo_url()

