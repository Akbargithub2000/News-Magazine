from django.db import models
from slugify import slugify
# from authors.models import AuthorDetailsModel
from django.contrib.auth.models import User

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.CharField(max_length=200)

    def save(self):
        self.slug = slugify(self.title)
        return super().save()
    
    def __str__(self):
        return self.title
    
class CategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category