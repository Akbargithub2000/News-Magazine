from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AuthorDetailsModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=15, null=True)
    image = models.ImageField(null=True, blank=True)
    specialized_in = models.CharField(null=True, blank=True, max_length=200)