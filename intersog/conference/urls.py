# coding: utf-8
from django.conf.urls import url, patterns, include 
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required   
from views import ConfList, ConfCreate, ConfView, ConfUpdate, ConfDelete, MemberCreate, ConfirmView, \
           MemberList, MemberView, MemberReporterList, RepresenterCreate, RepresenterList, RepresenterView, \
           ConfMemberList, ConfSponsorList, ConfReporterList, ConfArhivList

urlpatterns = [
    
    url(r'list/$', ConfList.as_view(), name='conf'),  
    url(r'list/arhiv$', login_required(ConfArhivList.as_view()), name='conf_arhiv'),  
    url(r'add/$', login_required(ConfCreate.as_view()), name='conf_add'),
    url(r'(?P<pk>\d+)/$', login_required(ConfView.as_view()), name='conf_view'),         
    url(r'(?P<pk>\d+)/edit/$', login_required(ConfUpdate.as_view()), name='conf_edit'),         
    url(r'(?P<pk>\d+)/delete/$', login_required(ConfDelete.as_view()), name='conf_delete'),
    url(r'delete/fail/$',login_required(TemplateView.as_view(template_name = 'delete_fail.html')), name='delete_fail'),
    

    url(r'(?P<pk>\d+)/member$', login_required(MemberCreate.as_view()), name='member'),
    
    url(r'member/confirm$',login_required(ConfirmView.as_view()), name='member_confirm'),
    url(r'member/refuse$',login_required(TemplateView.as_view(template_name = 'member_refuse.html')), name='member_refuse'),
    
    url(r'member/list$', login_required(MemberList.as_view()), name='member_list'), 
    url(r'member/(?P<pk>\d+)$', login_required(MemberView.as_view()), name='member_view'), 
    url(r'reporter/list$', login_required(MemberReporterList.as_view()), name='member_reporter_list'), 
    
    url(r'reprs/add$', login_required(RepresenterCreate.as_view()), name='representer'),
    url(r'reprs/already$', login_required(TemplateView.as_view(template_name = 'reps_already.html')), name='representer_already'),
    url(r'reprs/only-sponsor$', login_required(TemplateView.as_view(template_name = 'only_sponsor.html')), name='only_sponsor'),
    url(r'reprs/list$', login_required(RepresenterList.as_view()), name='reprs'),
    url(r'(?P<pk>\d+)/reprs/$', login_required(RepresenterView.as_view()), name='reprs_view'), 

    url(r'(?P<pk>\d+)/members$', login_required(ConfMemberList.as_view()), name='conf_member_list'), 
    url(r'(?P<pk>\d+)/sponsors$', login_required(ConfSponsorList.as_view()), name='conf_sponsor_list'), 
    url(r'(?P<pk>\d+)/reporters$', login_required(ConfReporterList.as_view()), name='conf_reporter_list'), 
    ]   