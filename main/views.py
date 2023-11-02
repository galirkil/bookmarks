from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from common.views import TitleMixin
from main.forms import BookmarkForm
from main.models import Bookmark
from main.tasks import get_bookmark_info


class IndexView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'Bookmarks - Главная'


class BookmarksListView(LoginRequiredMixin, TitleMixin, ListView):
    template_name = 'main/bookmarks.html'
    title = 'Bookmarks - Мои закладки'

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


@login_required
def add_bookmark(request):
    if request.method == 'POST':
        bookmark = Bookmark(user=request.user)
        form = BookmarkForm(data=request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.save()
            messages.success(request, 'Вы успешно добавили закладку!')
            get_bookmark_info.delay(request.POST['url'], request.user.id)
            return HttpResponseRedirect(reverse('main:add-bookmark'))
    else:
        form = BookmarkForm()
    context = {
        'form': form,
        'title': 'Bookmarks - Добавить закладку',
    }
    return render(request, 'main/add-bookmark.html', context)

