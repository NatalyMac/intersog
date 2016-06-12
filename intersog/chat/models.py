# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from swampdragon.models import SelfPublishModel
from .serializer import ChatSerializer


class Chat(SelfPublishModel, models.Model):

    class Meta(object):
        verbose_name = u"Чат"
        verbose_name_plural = u"Чат"
    
    serializer_class = ChatSerializer

    user_sent = models.ForeignKey(settings.AUTH_USER_MODEL,
        blank=True)

    user_receive_id = models.IntegerField(
        blank=True,
        verbose_name=u"Получатель")

    text = models.TextField(
       blank=True,)

    created = models.DateField(
        auto_now=False,
        auto_now_add=True,
        blank=True,
        verbose_name=u"Дата создания")

    def __unicode__(self):
        return '{}'.format(self.text)      


