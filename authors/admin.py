from django.contrib import admin
from authors.models import AuthorDetailsModel

# Register your models here.
@admin.register(AuthorDetailsModel)
class AuthorDetailsModelAdmin(admin.ModelAdmin):
    # list_display = ('user.username', 'phone_no')
    # search_fields = ('username', 'first_name', 'last_name')
    pass