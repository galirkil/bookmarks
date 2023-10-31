from django.contrib import admin

from main.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'user', )
    list_filter = ('user', )
