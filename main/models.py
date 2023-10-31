from django.db import models

from users.models import User


class Bookmark(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    url = models.URLField(default='https://')
    description = models.TextField()
    favicon = models.ImageField(upload_to='url_icons', null=True, blank=True)

    class Meta:
        verbose_name = 'закладка'
        verbose_name_plural = 'закладки'
        constraints = [
            models.UniqueConstraint(fields=['user', 'url'], name='unique_url')
        ]
