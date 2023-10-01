from django.db import models
from slugify import slugify
from authors.models import AuthorDetailsModel

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField()
    author = models.ForeignKey(AuthorDetailsModel, on_delete=models.CASCADE)
    body = models.TextField()
    category_id = models.CharField(max_length=200)

    def save(self):
        self.author = self.request.user
        self.slug = slugify(self.title)
        return super().save()
    
    def __str__(self):
        return self.title
    
class CategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category