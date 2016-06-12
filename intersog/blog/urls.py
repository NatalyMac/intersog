
# coding: utf-8
from django.conf.urls import url, patterns, include 
from views import NewsList, NewsCreate, NewsView, NewsUpdate, NewsDelete
from django.contrib.auth.decorators import login_required   

urlpatterns = [
    
    url(r'list/$', login_required(NewsList.as_view()), name='news'),  
    url(r'add/$', login_required(NewsCreate.as_view()), name='news_add'),
    url(r'(?P<pk>\d+)/$', login_required(NewsView.as_view()), name='news_view'),         
    url(r'(?P<pk>\d+)/edit/$', login_required(NewsUpdate.as_view()), name='news_edit'),         
    url(r'(?P<pk>\d+)/delete/$', login_required(NewsDelete.as_view()), name='news_delete'),         
   
]
