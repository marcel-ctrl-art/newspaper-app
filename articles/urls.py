from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesListView.as_view(), name='articles_list'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', views.ArticleEditView.as_view(), name='article_edit'),
    path('new/', views.ArticleCreateView.as_view(), name='article_create'),
]