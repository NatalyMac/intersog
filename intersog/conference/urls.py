# coding: utf-8
from django.conf.urls import url, patterns, include 
from django.views.generic.base import TemplateView
from views import ConfList, ConfCreate, ConfView, ConfUpdate, ConfDelete, MemberCreate, ConfirmView, \
           MemberList, MemberView, MemberReporterList, RepresenterCreate, RepresenterList, RepresenterView, \
           ConfMemberList, ConfSponsorList, ConfReporterList, ConfArhivList

from chat.views import ChatCreate

urlpatterns = [
    
    url(r'list/$', ConfList.as_view(), name='conf'),  
    url(r'list/arhiv$', ConfArhivList.as_view(), name='conf_arhiv'),  
    url(r'add/$', ConfCreate.as_view(), name='conf_add'),
    url(r'(?P<pk>\d+)/$', ConfView.as_view(), name='conf_view'),         
    url(r'(?P<pk>\d+)/edit/$', ConfUpdate.as_view(), name='conf_edit'),         
    url(r'(?P<pk>\d+)/delete/$', ConfDelete.as_view(), name='conf_delete'),
    url(r'delete/fail/$',TemplateView.as_view(template_name = 'delete_fail.html'), name='delete_fail'),
    

    url(r'(?P<pk>\d+)/member$', MemberCreate.as_view(), name='member'),
    
    url(r'member/confirm$',ConfirmView.as_view(), name='member_confirm'),
    url(r'member/refuse$',TemplateView.as_view(template_name = 'member_refuse.html'), name='member_refuse'),
    
    url(r'member/list$',MemberList.as_view(), name='member_list'), 
    url(r'member/(?P<pk>\d+)$',MemberView.as_view(), name='member_view'), 
    url(r'reporter/list$', MemberReporterList.as_view(), name='member_reporter_list'), 
    
    url(r'reprs/add$',RepresenterCreate.as_view(), name='representer'),
    url(r'reprs/already$',TemplateView.as_view(template_name = 'reps_already.html'), name='representer_already'),
    url(r'reprs/only-sponsor$',TemplateView.as_view(template_name = 'only_sponsor.html'), name='only_sponsor'),
    url(r'reprs/list$',RepresenterList.as_view(), name='reprs'),
    url(r'(?P<pk>\d+)/reprs/$',RepresenterView.as_view(), name='reprs_view'), 

    url(r'(?P<pk>\d+)/members$',ConfMemberList.as_view(), name='conf_member_list'), 
    url(r'(?P<pk>\d+)/sponsors$',ConfSponsorList.as_view(), name='conf_sponsor_list'), 
    url(r'(?P<pk>\d+)/reporters$',ConfReporterList.as_view(), name='conf_reporter_list'), 

    url(r'member/(?P<pk>\d+)/chat/$', ChatCreate.as_view(), name='chat_create'), 
    ]   