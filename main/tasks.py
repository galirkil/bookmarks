from celery import shared_task

from main.models import Bookmark
from main.parsers import get_description, get_title


@shared_task
def get_bookmark_info(url, user):
    bookmark = Bookmark.objects.get(url=url, user=user)
    bookmark.title = get_title(url)
    bookmark.description = get_description(url)
    bookmark.save()

