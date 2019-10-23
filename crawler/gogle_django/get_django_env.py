from crawler.models import ImageLink
import django
import re
from collections import deque
from bs4 import BeautifulSoup
import requests
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()


# imageObj = ImageLink(web_link="https://naver.com", img_link="test")
# imageObj.save()


def parser(queue, result):
    while queue:
        path = queue.pop()
        url = domain + path

        # 큐에서 꺼낸 링크에 get 요청
        try:
            req = requests.get(url=url)
            html = req.text
        except requests.RequestException:
            continue
        else:
            result.add(url)

        soup = BeautifulSoup(html, 'html.parser')

        # 링크의 이미지 찾기
        images = soup.find_all('img')
        for image in images:
            if 'src' in image.attrs:
                pat = re.compile('(?=https://).*')
                if pat.match(image.attrs['src']):
                    yield url, image.attrs['src']
                elif image.attrs['src'].startswith('//'):
                    yield url, 'https:' + image.attrs['src']
                elif image.attrs['src'].startswith('/'):
                    yield url, domain + image.attrs['src']
                else:
                    continue

        # 링크의 다른 내부 링크 찾아 큐에 넣기
        links = soup.find_all('a')
        for link in links:
            if 'href' in link.attrs:
                if domain + link.attrs['href'] not in result:
                    pat = re.compile('((?!http://|https://).)*')
                    if pat.match(link.attrs['href']).group():
                        queue.append(link.attrs['href'])


domain = 'https://en.wikipedia.org'
queue = deque(['/wiki/Main_Page'])
result = set()

p = parser(queue, result)

for i in p:
    print(i)
