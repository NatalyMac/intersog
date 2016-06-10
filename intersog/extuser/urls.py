# coding: utf-8
from django.conf.urls import url, patterns, include 
from views import UserView, UserUpdate, UserDelete


urlpatterns = [
    
    url(r'(?P<pk>\d+)/$', UserView.as_view(), name='user_view'),         
    url(r'(?P<pk>\d+)/edit/$', UserUpdate.as_view(), name='user_edit'),         
    url(r'(?P<pk>\d+)/delete/$', UserDelete.as_view(), name='user_delete')
    
    ]   