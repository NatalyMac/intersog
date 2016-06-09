# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, first_name, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password, first_name, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    
    objects = UserManager()

    MEMBER    = u"member"
    SPONSOR   = u"sponsor"
    TYPE_OF_USER = (
        (MEMBER, u'Участник'),
        (SPONSOR, u'Споносор'),) 
    
    USERNAME_FIELD = 'email'
    
    email = models.EmailField(
    	unique=True,
    	verbose_name=u"Email")
    
    joined = models.DateTimeField(
    	auto_now_add=True)
    
    is_active = models.BooleanField(
    	default=True)
    
    is_admin = models.BooleanField(
    	default=False) 
    

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Имя")

    last_name = models.CharField(
       max_length=256,
       blank=False,
       verbose_name=u"Фамилия")
  
    occupation = models.CharField(
       max_length=256,
       blank=False,
       verbose_name=u"Вид деятельности")

    role = models.CharField(
        max_length=15,
        choices=TYPE_OF_USER,
        default=MEMBER,
        blank=False,
        verbose_name=u"Роль",)     

    photo = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

    created = models.DateField(
        auto_now=False,
        auto_now_add=True,
        blank=True,
        verbose_name=u"Дата создания")

    modified = models.DateField(
        auto_now=True,
        auto_now_add=False,
        blank=True,
        verbose_name=u"Дата изменения")     

    def get_full_name(self):
        return unicode(self.email)

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return unicode(self.email)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)               
    
    def __unicode__(self):
        return unicode(self.email)
    
    def get_absolute_url(self):
        return u'accounts/{}'.format(self.id )
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


