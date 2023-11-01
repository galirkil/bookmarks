from django.urls import path

from main.views import BookmarksListView, add_bookmark

app_name = 'main'

urlpatterns = [
    path('my-bookmarks/', BookmarksListView.as_view(), name='my-bookmarks'),
    path('add-bookmark/', add_bookmark, name='add-bookmark')
]
