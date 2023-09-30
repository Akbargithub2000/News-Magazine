from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from article.models import ArticleModel
from article.forms import ArticleForm

# Create your views here.
class AddArticleView(SuccessMessageMixin, CreateView):
    model = ArticleModel
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = '/articles/'
    success_message = "Your article has been added."

class UpdateArticleView(SuccessMessageMixin, UpdateView):
    model = ArticleModel
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = '/articles/'
    success_message = "Your changes has been saved."