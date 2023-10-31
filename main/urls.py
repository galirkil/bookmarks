from django.urls import path

from main.views import BookmarkCreateView, BookmarksListView

app_name = 'main'

urlpatterns = [
    path('my-bookmarks/', BookmarksListView.as_view(), name='my-bookmarks'),
    path('add-bookmark/', BookmarkCreateView.as_view(), name='add-bookmark')
]
