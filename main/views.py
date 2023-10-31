from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from common.views import TitleMixin
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


class BookmarkCreateView(LoginRequiredMixin, TitleMixin, SuccessMessageMixin, CreateView):
    template_name = 'main/add-bookmark.html'
    title = 'Bookmarks - Добавить закладку'
    model = Bookmark
    fields = ('url', )
    success_url = reverse_lazy('main:add-bookmark')
    success_message = 'Вы успешно добавили новую закладку!'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        get_bookmark_info.delay(self.request.POST['url'], self.request.user.id)
        return response

