# coding: utf-8
from django.conf.urls import url, patterns, include 
from views import UserView, UserUpdate, UserDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
    
    url(r'(?P<pk>\d+)/$', login_required(UserView.as_view()), name='user_view'),         
    url(r'(?P<pk>\d+)/edit/$', login_required(UserUpdate.as_view()), name='user_edit'),         
    url(r'(?P<pk>\d+)/delete/$', login_required(UserDelete.as_view()), name='user_delete')
    
    ]   