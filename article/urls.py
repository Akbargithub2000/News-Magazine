from django.urls import path
from article.views import AddArticleView, UpdateArticleView

urlpatterns = [
    path('article/add/', AddArticleView.as_view(), name="add-article"),
    path('article/<slug:slug>/edit/', UpdateArticleView.as_view(), name="update-article"),
]