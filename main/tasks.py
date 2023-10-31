import os
from urllib import request

from celery import shared_task
from django.core.files import File

from main.models import Bookmark
from main.parsers import get_description, get_favicon_url, get_title


@shared_task
def get_bookmark_info(url: str, user_id: int) -> None:
    bookmark = Bookmark.objects.get(url=url, user=user_id)
    bookmark.title = get_title(url)
    bookmark.description = get_description(url)
    bookmark.save()
    image_url = get_favicon_url(url)
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0')]
    request.install_opener(opener)
    image = request.urlretrieve(image_url)
    bookmark.favicon.save(os.path.basename(image_url), File(open(image[0], 'rb')))
