from django.forms import ModelForm

from main.models import Bookmark


class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ('url', )
