from django.shortcuts import render
from django.views.generic import ListView

from .modles import Article

class ArticlesListView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'articles_list.html'