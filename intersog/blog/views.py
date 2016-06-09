# coding: utf-8
from django.core.paginator          import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic           import ListView
from django.views.generic.edit      import CreateView, UpdateView, DeleteView
from django.views.generic.detail    import DetailView
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers       import reverse_lazy 

from models import News

class NewsList(ListView):
    model = News
    context_object_name = 'news'
    template_name = "news_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        print context

        list_news = News.objects.all()
        paginator = Paginator(list_news, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            list_news = paginator.page(page)
        except PageNotAnInteger:
            list_news = paginator.page(1)
        except EmptyPage:
            list_news = paginator.page(paginator.num_pages)
        context['list_news'] = list_news
        return context


class NewsCreate(CreateView):
    model = News
    fields = ['title', 
              'text']
    template_name = "news_add.html"
    context_object_name = 'news'
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewsCreate, self).dispatch(*args, **kwargs)

class NewsView(DetailView):
    model = News
    template_name = "news_view.html"
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        return context

class NewsUpdate(UpdateView):
    model = News
    fields = ['title', 
              'text']
    template_name = "news_edit.html"
    context_object_name = 'news'
     
    #@method_decorator(login_required)
    #def dispatch(self, *args, **kwargs):
    #    return super(NewsUpdate, self).dispatch(*args, **kwargs)

class NewsDelete(DeleteView):
    model = News
    
    def get_success_url(self):
        return reverse_lazy('blog:news')    
