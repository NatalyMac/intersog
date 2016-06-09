
# coding: utf-8
from django.conf.urls import url, patterns, include 
from views import NewsList, NewsCreate, NewsView, NewsUpdate, NewsDelete

urlpatterns = [
    
    url(r'list/$', NewsList.as_view(), name='news'),  
    url(r'add/$', NewsCreate.as_view(), name='news_add'),
    url(r'(?P<pk>\d+)/$', NewsView.as_view(), name='news_view'),         
    url(r'(?P<pk>\d+)/edit/$', NewsUpdate.as_view(), name='news_edit'),         
    url(r'(?P<pk>\d+)/delete/$', NewsDelete.as_view(), name='news_delete'),         
   
]
