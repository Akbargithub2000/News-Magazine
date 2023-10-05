from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, TemplateView, DetailView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from article.models import ArticleModel
from article.forms import ArticleForm
from django.contrib import messages

# Create your views here.
class AddArticleView(View):
    model = ArticleModel
    template_name = "articles/article_form.html"
    form_class = ArticleForm
    success_url = '/articles/'
    success_message = "Your article has been added."

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                image = request.FILES.get('image')
                body = form.cleaned_data.get('body')
                category = form.cleaned_data.get('category')

                article = ArticleModel(title=title, image=image, body=body, category=category, author_id=request.user.id)
                article.save()
                messages.success(request, "Article successfully added.")
                return redirect('add-article')
            else:
                messages.error(request, "Enter valid data")
                return redirect('add-article')
        form = ArticleModel()
        return render(request, self.template_name, {'form': form})

class UpdateArticleView(SuccessMessageMixin, UpdateView):
    model = ArticleModel
    template_name = "articles/article_form.html"
    form_class = ArticleForm
    success_url = '/authors/homepage/'
    success_message = "Your changes has been saved."

class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'

class DeleteArticleView(DeleteView):
    model = ArticleModel
    success_url = '/authors/homepage/'
    context_object_name = 'article'
    template_name = 'articles/article_delete_form.html'

class ArticleViewByCategory(ListView):
    model = ArticleModel
    paginate_by = 24
    context_object_name = 'article'
    template_name = 'articles/articles_category.html'

    def get_queryset(self):
        return ArticleModel.objects.filter(category__icontains = self.kwargs.get('category'))
    
class ArticlesView(ListView):
    model = ArticleModel
    paginate_by = 24
    context_object_name = 'article'
    template_name = 'articles/home.html'