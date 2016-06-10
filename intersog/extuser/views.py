# coding: utf-8
from django.views.generic.edit      import UpdateView, DeleteView
from django.views.generic.detail    import DetailView
from django.core.urlresolvers       import reverse_lazy 
from django.contrib.auth.mixins     import LoginRequiredMixin

from models import User
from conference.models import Representer
from common.my_paginator import my_pages


# операции со своим профилем
class UserView(LoginRequiredMixin, DetailView):
    model = User
    fields = ['first_name',
              'last_name',
              'occupation', 
               'photo',
               'role',
               'email']
    template_name = "user_view.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        list_reprs =  Representer.objects.filter(representer_id = self.request.user.id)
        list_id_sponsor = [item.sponsor for item in list_reprs]
        list_user_sponsor = User.objects.filter(id__in=list_id_sponsor)
        context['reprs'] = list_user_sponsor
        return context
    


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name',
              'last_name',
              'occupation', 
              'photo', 
              'role',
              'email'
               ]
    template_name = "user_edit.html"
    context_object_name = 'user'



class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    
    def get_success_url(self):
        return reverse_lazy('accounts:user')   


