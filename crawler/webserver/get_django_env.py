import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# get django environment
import django

django.setup()

from crawler.models import ImageLink

imageObj = ImageLink(web_link="https://naver.com", img_link="test")
imageObj.save()

