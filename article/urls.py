from django.urls import path
from article.views import AddArticleView, UpdateArticleView, ArticleDetailView, DeleteArticleView, ArticleViewByCategory, ArticlesView

# app_name = 'article'

urlpatterns = [
    # path('', ArticlesView.as_view(), name='articles'),
    path('article/add/', AddArticleView.as_view(), name="add-article"),
    path('article/<slug:slug>/edit/', UpdateArticleView.as_view(), name="update-article"),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name="article-details"),
    path('article/<slug:slug>/delete', DeleteArticleView.as_view(), name="delete-article"),
    path('<str:category>/article/', ArticleViewByCategory.as_view(), name='article-category')
]