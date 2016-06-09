# coding: utf-8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def my_pages(list_item, paginate_by, page):
    paginator = Paginator(list_item, paginate_by)
    try:
        list_item = paginator.page(page)
    except PageNotAnInteger:
        list_item = paginator.page(1)
    except EmptyPage:
        list_item = paginator.page(paginator.num_pages)
    return list_item