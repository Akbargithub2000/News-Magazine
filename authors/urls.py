from django.urls import path
from authors.views import LoginView, AddAuthorView

urlpatterns = [
    path('login/', LoginView.as_view(), name='author_login'),
    path('sign_up/', AddAuthorView.as_view(), name='add-author'),
]