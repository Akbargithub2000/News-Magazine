from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from article.models import ArticleModel
from article.forms import ArticleForm
from django.contrib import messages

# Create your views here.
class AddArticleView(View):
    model = ArticleModel
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = '/articles/'
    success_message = "Your article has been added."

    def post(self, request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                image = request.FILES.get('image')
                body = form.cleaned_data.get('body')
                category_id = form.cleaned_data.get('category_id')

                article = ArticleModel(title=title, image=image, body=body, category_id=category_id, author_id=request.user)
                messages.success(request, "Article successfully added.")
                return redirect('add-article')
            else:
                messages.error(request, "Enter valid data")
                return redirect('add-article')
        form = ArticleModel()
        return render(request, self.template_name, {'form': form})

class UpdateArticleView(SuccessMessageMixin, UpdateView):
    model = ArticleModel
    template_name = "article_form.html"
    form_class = ArticleForm
    success_url = '/articles/'
    success_message = "Your changes has been saved."