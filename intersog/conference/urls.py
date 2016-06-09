# coding: utf-8
from django.conf.urls import url, patterns, include 
from django.views.generic.base import TemplateView
from views import ConfList, ConfCreate, ConfView, ConfUpdate, ConfDelete, MemberCreate, ConfirmView, \
           MemberList, MemberView, MemberReporterList, RepresenterCreate, RepresenterList, ConfMemberList, \
           ConfSponsorList, ConfReporterList, ConfArhivList

from django.contrib.auth.decorators import login_required
from chat.views import ChatCreate

urlpatterns = [
    
    url(r'list/$', login_required(ConfList.as_view()), name='conf'),  
    url(r'list/arhiv$', login_required(ConfArhivList.as_view()), name='conf_arhiv'),  
    url(r'add/$', login_required(ConfCreate.as_view()), name='conf_add'),
    url(r'(?P<pk>\d+)/$', login_required(ConfView.as_view()), name='conf_view'),         
    url(r'(?P<pk>\d+)/edit/$', login_required(ConfUpdate.as_view()), name='conf_edit'),         
    url(r'(?P<pk>\d+)/delete/$', login_required(ConfDelete.as_view()), name='conf_delete'),
    url(r'(?P<pk>\d+)/member$',login_required(MemberCreate.as_view()), name='member'),
    
    url(r'member/confirm$',ConfirmView.as_view(), name='member_confirm'),
    url(r'member/refuse$',TemplateView.as_view(template_name = 'member_refuse.html'), name='member_refuse'),
    
    url(r'member/list$',MemberList.as_view(), name='member_list'), 
    url(r'member/(?P<pk>\d+)$',MemberView.as_view(), name='member_view'), 
    url(r'reporter/list$', MemberReporterList.as_view(), name='member_reporter_list'), 
    
    url(r'reprs/add$',RepresenterCreate.as_view(), name='representer'),
    url(r'reprs/already$',TemplateView.as_view(template_name = 'reps_already.html'), name='representer_already'),
    url(r'reprs/list$',RepresenterList.as_view(), name='reprs'),

    url(r'(?P<pk>\d+)/members$',ConfMemberList.as_view(), name='conf_member_list'), 
    url(r'(?P<pk>\d+)/sponsors$',ConfSponsorList.as_view(), name='conf_sponsor_list'), 
    url(r'(?P<pk>\d+)/reporters$',ConfReporterList.as_view(), name='conf_reporter_list'), 

    url(r'member/(?P<pk>\d+)/chat/$', login_required(ChatCreate.as_view()), name='chat_create'), 
    ]   