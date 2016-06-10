# coding: utf-8
from __future__ import unicode_literals

from django.db      import models
#from django.contrib.auth.models import User
from django.conf    import settings 
from datetime       import datetime, timedelta, date, time 
from extuser.models import User

class Conference(models.Model):
    
    ARCHIV_DAYS = 3
    
    class Meta(object):
        verbose_name = u"Конференция"
        verbose_name_plural = u"Конференции"
    
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Название")

    theme = models.TextField(
        blank=True,
        verbose_name=u"Содержание")

    place = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Место проведения")

    date_begin = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=False,
        verbose_name=u"Дата начала")

    date_end = models.DateField(
        auto_now=False,
        auto_now_add=False,
        blank=False,
        verbose_name=u"Дата завершения")

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
        return u'{}'.format(self.name)

    def get_absolute_url(self):
        return u'/conf/{}'.format(self.id)   
     
    @classmethod       
    def get_current_conf(cls):
        date = datetime.now()
        date = date.date()-timedelta(days = cls.ARCHIV_DAYS)
        list_conf = cls.objects.filter(date_end__gt = date)
        return list_conf
    
    @classmethod       
    def get_arhiv_conf(cls):
        date = datetime.now()
        date = date.date()-timedelta(days = cls.ARCHIV_DAYS)
        list_conf = cls.objects.filter(date_end__lt = date)
        return list_conf
    



class MemberConference(models.Model):

    LISTENER    = u"listener"
    REPORTER    = u"reporter"
    TYPE_OF_USER = (
        (LISTENER, u'Слушатель'),
        (REPORTER, u'Докладчик'),)

    class Meta(object):
        verbose_name = u"Участник конференции"
        verbose_name_plural = u"Участники конференции"
    
    unique_together = ("member_id", "conference_id", "role")

    member = models.ForeignKey(settings.AUTH_USER_MODEL,
       verbose_name=u"Участник",
       blank=False,
       null=True,
       on_delete=models.PROTECT)  
  

    conference = models.ForeignKey('Conference',
       verbose_name=u"Конференция",
       blank=False,
       null=True,
       on_delete=models.PROTECT)

    role = models.CharField(
        max_length=15,
        choices=TYPE_OF_USER,
        default=LISTENER,
        blank=False,
        verbose_name=u"Роль")

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
        return u'{}{}{}'.format(self.member.first_name, self.conference, self.role)

class Representer(models.Model):
    
    class Meta(object):
        verbose_name = u"Представитель спонсора"
        verbose_name_plural = u"Представители спонсора"
    
    unique_together = ("representer", "sponsor")

    representer = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name=u"Представитель",
        blank=True,
        null=True,
        on_delete=models.PROTECT 
        ) 
    
    sponsor = models.IntegerField(
        verbose_name=u"Спонсор",
        blank=True,
        ) 

    def __unicode__(self):
        return u'{}{}'.format(self.representer, self.sponsor)