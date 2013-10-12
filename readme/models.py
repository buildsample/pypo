from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from tld import get_tld
from django.core.urlresolvers import reverse


class Item(models.Model):
    url = models.URLField()
    title = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    readable_article = models.TextField(null=True)

    @property
    def summary(self):
        return strip_tags(self.readable_article)[:300]

    @property
    def domain(self):
        return get_tld(self.url.encode('utf-8'), fail_silently=True)

    def get_absolute_url(self):
        return reverse('item_view', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('item_delete', args=[str(self.id)])
