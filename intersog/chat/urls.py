# coding: utf-8
from django.conf.urls import url, patterns, include 
from django.views.generic.base import TemplateView

from views import ChatList, ChatAddView

urlpatterns = [
    
    url(r'user/$', ChatList.as_view(), name='chat_user'), 
    
    url(r'(?P<pk>\d+)$', ChatAddView.as_view(), name='chat'),
    
    ]
