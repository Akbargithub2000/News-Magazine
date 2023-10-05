from django.urls import path
from authors.views import LoginView, AddAuthorView, EditAuthorDetailsView, ProfileView, AuthorHomePage, LogoutView, AdminLoginView, DeleteAuthorView, AllAuthorsView, AuthorProfileView

urlpatterns = [
    path('admin-login/', AdminLoginView.as_view(), name='admin_login'),
    path('login/', LoginView.as_view(), name='author_login'),
    path('sign_up/', AddAuthorView.as_view(), name='add-author'),
    path('logout/', LogoutView.as_view(), name='author-logout'),
    path('<int:pk>/edit_profile/', EditAuthorDetailsView.as_view(), name='edit-author-profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('homepage/', AuthorHomePage.as_view(), name='homepage'),
    path('authors-all/', AllAuthorsView.as_view(), name="all-authors"),
    path('<int:pk>/view-author/', AuthorProfileView.as_view(), name="author-profile"),
    path('<int:id>/delete-author/', DeleteAuthorView.as_view(), name="delete-author"),
]