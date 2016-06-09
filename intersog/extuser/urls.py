# coding: utf-8
from django.conf.urls import url, patterns, include 
from django.contrib.auth.decorators import login_required
from views import UserList, UserView, UserUpdate, UserDelete ,UserCreate, ProfileView

urlpatterns = [
    
    url(r'list/$', login_required(UserList.as_view()), name='user'),  
    url(r'add/$', login_required(UserCreate.as_view()), name='user_add'),
    url(r'profile/$', login_required(ProfileView.as_view()), name='profile_view'), 
    url(r'(?P<pk>\d+)/$', login_required(UserView.as_view()), name='user_view'),         
    url(r'(?P<pk>\d+)/edit/$', login_required(UserUpdate.as_view()), name='user_edit'),         
    url(r'(?P<pk>\d+)/delete/$', login_required(UserDelete.as_view()), name='user_delete')
    
    ]   