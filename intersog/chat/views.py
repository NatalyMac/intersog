# coding: utf-8
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit      import CreateView, UpdateView, DeleteView
from django.views.generic           import ListView
from django.shortcuts               import redirect
from django.core.urlresolvers       import reverse_lazy, reverse

from models import Chat
from extuser.models import User
from conference.models import MemberConference
from common.my_paginator import my_pages



class ChatCreate(CreateView):
    
    model = Chat
    fields = ['text']
    template_name = "chat.html"
    
    def form_valid(self, form):
        form.instance.user_sent = User.objects.get(id=self.request.user.id)
        user_id = int(self.request.path.split('/')[3])
        mem = MemberConference.objects.get(id=user_id)
        form.instance.user_receive_id = User.objects.get(id=mem.member.id).id
        form.instance.save()    
        return redirect(self.get_success_url())                                              
          
    def get_success_url(self):
        return reverse_lazy('conf:member_list')  

class ChatList(ListView):
    
    model = Chat
    context_object_name = 'chats'
    template_name = "chat_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ChatList, self).get_context_data(**kwargs)

        list_chat = Chat.objects.filter(user_receive_id = self.request.user.id)
        print list_chat
        print self.request.user.id
        page = self.request.GET.get('page')
        context['chats'] = my_pages(list_chat, self.paginate_by, page)
        return context