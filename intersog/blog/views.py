# coding: utf-8
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic           import ListView
from django.views.generic.edit      import CreateView, UpdateView, DeleteView
from django.views.generic.detail    import DetailView
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers       import reverse_lazy 
from common.my_paginator            import my_pages

from models import News

class NewsList(LoginRequiredMixin, ListView):
    model = News
    context_object_name = 'news'
    template_name = "news_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        print context
        list_news = News.objects.all()
        page = self.request.GET.get('page')
        context['list_news'] = my_pages(list_news, self.paginate_by, page)
        return context


class NewsCreate(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 
              'text']
    template_name = "news_add.html"
    context_object_name = 'news'
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewsCreate, self).dispatch(*args, **kwargs)

class NewsView(LoginRequiredMixin, DetailView):
    model = News
    template_name = "news_view.html"
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        return context

class NewsUpdate(LoginRequiredMixin, UpdateView):
    model = News
    fields = ['title', 
              'text']
    template_name = "news_edit.html"
    context_object_name = 'news'
     
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewsUpdate, self).dispatch(*args, **kwargs)

class NewsDelete(LoginRequiredMixin, DeleteView):
    model = News
    
    def get_success_url(self):
        return reverse_lazy('blog:news')    
