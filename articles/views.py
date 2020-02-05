from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView, ListView

from .models import Article


class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('article_list')


class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    model = Article
    context_object_name = 'articles'


class ArticlesListView(ListView):
    model = Article
    paginate_by = 3
    template_name = 'articles_list.html'
    context_object_name = 'articles'
