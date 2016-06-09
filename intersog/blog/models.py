# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class News(models.Model):

    class Meta(object):
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"
        ordering = ['-created']
    
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Заголовок")

    text = models.TextField(
       blank=True,
        verbose_name=u"Текст")
    
    created = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        blank=True,
        verbose_name=u"Дата создания")

    modified = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        blank=True,
        verbose_name=u"Дата изменения")

    def __unicode__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return u'/blog/{}'.format(self.id)
    
