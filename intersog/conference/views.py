# coding: utf-8
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers       import reverse_lazy, reverse
from django                         import forms
from django.utils.decorators        import method_decorator
from django.views.generic.base      import TemplateView
from django.views.generic           import ListView
from django.views.generic.edit      import CreateView, UpdateView, DeleteView
from django.views.generic.detail    import DetailView
from django.shortcuts               import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date, time 


from models import Conference, MemberConference, Representer
from extuser.models import User
from common.my_paginator import my_pages


class ConfList(ListView):
    
    model = Conference
    context_object_name = 'conferences'
    template_name = "conf_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ConfList, self).get_context_data(**kwargs)
        date = datetime.now()
        date = date.date()-timedelta(days=3)
        list_conf = Conference.objects.filter(date_end__gt=date)
        page = self.request.GET.get('page')
        context['conferences'] = my_pages(list_conf, self.paginate_by, page)
        return context

class ConfArhivList(ListView):
    
    model = Conference
    context_object_name = 'conferences'
    template_name = "conf_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ConfArhivList, self).get_context_data(**kwargs)
        date = datetime.now()
        date = date.date()+timedelta(days=3)
        list_conf = Conference.objects.filter(date_end__lt=date)
        page = self.request.GET.get('page')
        context['conferences'] = my_pages(list_conf, self.paginate_by, page)
        return context



class ConfCreate(CreateView):
    
    model = Conference
    fields = ['name', 
              'place',
              'theme', 
              'date_begin',
              'date_end']

    template_name = "conf_add.html"
    context_object_name = 'conference'
   
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsCreate, self).dispatch(*args, **kwargs)


class ConfView(DetailView):
    
    model = Conference
    template_name = "conf_view.html"
    context_object_name = 'conference'

    def get_context_data(self, **kwargs):
        context = super(ConfView, self).get_context_data(**kwargs)
        return context


class ConfUpdate(UpdateView):
    
    model = Conference
    fields = ['name', 
              'place',
              'theme', 
              'date_begin',
              'date_end']

    template_name = "conf_edit.html"
    context_object_name = 'conference'
     
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewsUpdate, self).dispatch(*args, **kwargs)


class ConfDelete(DeleteView):
    
    model = Conference
    
    def get_success_url(self):
        return reverse_lazy('conf:news')    


class MemberCreate(CreateView):
    
    model = MemberConference
    fields = ['role']
    template_name = "member.html"
    
    def form_valid(self, form):
        form.instance.member = User.objects.get(id=self.request.user.id)
        conference_id = int(self.request.path.split('/')[2])
        form.instance.conference = Conference.objects.get(id=conference_id)
        self.request.session['conferenceid'] = conference_id
        self.request.session['role'] = form.instance.role
        try:
            form.instance.save()
        except:
            return redirect(reverse('conf:member_refuse'))                
        
        return redirect(self.get_success_url())                                                  
          
    def get_success_url(self):
        return reverse_lazy('conf:member_confirm')  


class ConfirmView(TemplateView):

    template_name = "member_confirm.html"
    
    def get_context_data(self, **kwargs):
        context = super(ConfirmView, self).get_context_data(**kwargs)
        conference_id =  self.request.session['conferenceid']
        context['conference'] = Conference.objects.get(id=conference_id)
        context['role'] = self.request.session['role']
        context['member'] = User.objects.get(id=self.request.user.id) #спонсор или участник
        return context


class MemberList(ListView):
    
    model = MemberConference
    context_object_name = 'members'
    template_name = "member_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(MemberList, self).get_context_data(**kwargs)
        list_members = MemberConference.objects.distinct('member_id')
        page = self.request.GET.get('page')
        context['members'] = my_pages(list_members, self.paginate_by, page)
        return context

class MemberReporterList(ListView):
    
    model = MemberConference
    context_object_name = 'members'
    template_name = "member_reporter_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(MemberReporterList, self).get_context_data(**kwargs)
        list_members = MemberConference.objects.filter(role = "reporter").distinct('member_id')
        page = self.request.GET.get('page')
        context['members'] = my_pages(list_members, self.paginate_by, page)
        # if list_member will be without distinct
        return context


class MemberView(DetailView):
    
    model = MemberConference
    template_name = "member_view.html"
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super(MemberView, self).get_context_data(**kwargs)
        return context

class RepresenterCreate(CreateView):
    
    model = Representer
    fields = '__all__'
    template_name = "member_view.html"
    
    def form_valid(self, form):
        representer_id = self.request.POST.get('reprs')
        form.instance.representer = User.objects.get(id=representer_id)
        form.instance.sponsor = self.request.user.id

        if  int(representer_id) == int(form.instance.sponsor):
            return redirect(reverse('conf:representer_already'))     
        try:
            form.instance.save()
        except:
            return redirect(reverse('conf:representer_already'))                
        
        return redirect(self.get_success_url())   

    def get_success_url(self):
        return reverse_lazy('conf:member_reporter_list')  

class RepresenterList(ListView):
    
    model = Representer
    context_object_name = 'representers'
    template_name = "representer_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(RepresenterList, self).get_context_data(**kwargs)
        sponsor = User.objects.get(id=self.request.user.id).id
        list_members  =  Representer.objects.filter(sponsor = sponsor)
        page = self.request.GET.get('page')
        context['representers'] = my_pages(list_members, self.paginate_by, page)
        #list_ == distinct
        return context


class ConfMemberList(ListView):
    
    model = MemberConference
    context_object_name = 'members'
    template_name = "conf_detail_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ConfMemberList, self).get_context_data(**kwargs)
        conference_id = int(self.request.path.split('/')[2])
        list_members = MemberConference.objects.filter(conference=conference_id)
        page = self.request.GET.get('page')
        context['members'] = my_pages(list_members, self.paginate_by, page)
        context['conference_id'] = conference_id 
        return context

class ConfSponsorList(ListView):
    
    model = MemberConference
    context_object_name = 'members'
    template_name = "conf_detail_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ConfSponsorList, self).get_context_data(**kwargs)
        conference_id = int(self.request.path.split('/')[2])
        list_members = MemberConference.objects.filter(conference=conference_id)
        list_id_sponsor = [item.member_id for item in list_members]
        list_user_sponsor = User.objects.filter(id__in=list_id_sponsor, role='sponsor')
        print list_user_sponsor
        page = self.request.GET.get('page')
        context['members'] = my_pages(list_user_sponsor, self.paginate_by, page)
        context['conference_id'] = conference_id 
        return context


class ConfReporterList(ListView):
    
    model = MemberConference
    context_object_name = 'members'
    template_name =  "conf_detail_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ConfReporterList, self).get_context_data(**kwargs)
        conference_id = int(self.request.path.split('/')[2])
        list_members = MemberConference.objects.filter(conference=conference_id, role = 'reporter')
        page = self.request.GET.get('page')
        context['members'] = my_pages(list_members, self.paginate_by, page)
        context['conference_id'] = conference_id 
        return context