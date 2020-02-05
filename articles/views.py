from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article_create.html'
    model = Article
    fields = ['title', 'text']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_delete.html'
    model = Article
    success_url = reverse_lazy('articles_list')


class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article


class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    paginate_by = 3
    template_name = 'articles_list.html'
    context_object_name = 'articles'


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'text']
