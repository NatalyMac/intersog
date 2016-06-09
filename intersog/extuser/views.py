# coding: utf-8
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic           import ListView
from django.views.generic.edit      import CreateView, UpdateView, DeleteView
from django.views.generic.detail    import DetailView
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers       import reverse_lazy 

from models import User
from conference.models import Representer
from common.my_paginator import my_pages


class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name = "user_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        list_user = User.objects.all()
        page = self.request.GET.get('page')
        context['list_user'] = my_pages(list_user, self.paginate_by, page)
        return context


class UserCreate(CreateView):
    model = User
    fields = '__all__'
    template_name = "user_add.html"
    context_object_name = 'user'
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(userCreate, self).dispatch(*args, **kwargs)      


class ProfileView(DetailView):
    model = User
    fields = ['first_name',
              'last_name',
              'occupation', 
               'photo']
    template_name = "profile_view.html"
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
            context = super(ProfileView, self).get_context_data(**kwargs)
            user_id = self.request.user.id
            list_reprs =  Representer.objects.filter(representer_id = user_id)
            list_id_sponsor = [item.sponsor for item in list_reprs]
            list_user_sponsor = User.objects.filter(id__in=list_id_sponsor)
            context['reprs'] = list_user_sponsor
            context['profile'] = User.objects.get(id=user_id)
            return context

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id) 



class UserView(DetailView):
    model = User
    fields = ['first_name',
              'last_name',
              'occupation', 
               'photo']
    template_name = "user_view.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        
        user_id = int(self.request.path.split('/')[2])
        list_reprs =  Representer.objects.filter(representer_id = user_id)
        list_id_sponsor = [item.sponsor for item in list_reprs]
        list_user_sponsor = User.objects.filter(id__in=list_id_sponsor)
        context['reprs'] = list_user_sponsor
        context['user'] = User.objects.get(id=user_id)
        return context



class UserUpdate(UpdateView):
    model = User
    fields = ['first_name',
              'last_name',
              'occupation', 
               'photo']
    template_name = "user_edit.html"
    context_object_name = 'user'

     
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(userUpdate, self).dispatch(*args, **kwargs)



class UserDelete(DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse_lazy('accounts:user')    
