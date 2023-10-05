from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, TemplateView, DetailView
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authors.forms import LoginForm, SignUpForm, EditProfileForm
from authors.models import AuthorDetailsModel
from article.models import ArticleModel

# Create your views here.
class LoginView(View):
    template_name = 'authors/login_form.html'
    form_class = LoginForm
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')

                if not User.objects.filter(username=username).exists():
                    messages.error(request, "Invalid Username")
                    return redirect('admin_login')

                user = authenticate(username=username, password=password)

                if user is None:
                    messages.error(request, "Invalid Password.")
                    return redirect('admin_login')

                login(request, user)
                messages.success(request, "Login Successful.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid Form.")
                return redirect('admin_login')
        login_form = LoginForm()
        return render(request, self.template_name, {'form': login_form})

class AdminLoginView(View):
    template_name = 'authors/login_form.html'
    form_class = LoginForm
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        if request.method == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')

                if not User.objects.filter(username=username).exists():
                    messages.error(request, "Invalid Username")
                    return redirect('author_login')

                user = authenticate(username=username, password=password)

                if user is None:
                    messages.error(request, "Invalid Password.")
                    return redirect('author_login')
                if not user.is_superuser:
                    messages.error(request, "Not an Admin. Login as an Author")
                login(request, user)
                messages.success(request, "Login Successful.")
                return redirect('/')
            else:
                messages.error(request, "Invalid Form.")
                return redirect('author_login')
        login_form = LoginForm()
        return render(request, self.template_name, {'form': login_form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
class AddAuthorView(View):
    template_name = 'authors/sign_up.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                phone_no = form.cleaned_data.get('phone_no')
                image = request.FILES.get('image')
                password = form.cleaned_data.get('password')
                confirm_password = form.cleaned_data.get('confirm_password')

                if password != confirm_password:
                    messages.error(request, "Password and Confirm password must match.")
                    return redirect('sign_up/')
                
                if User.objects.filter(username=username).exists():
                    messages.error(request, "Username already exists.")
                    return redirect('add-author')

                user = User(username=username, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)

                author_details = AuthorDetailsModel(user=user, phone_no=phone_no, image=image)

                user.save()
                author_details.save()

                messages.success(request, 'Successfully registered.')
                return redirect('add-author')
            else:
                messages.error(request, 'Enter valid data')
                return redirect('add-author')
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})
    
class EditAuthorDetailsView(SuccessMessageMixin, UpdateView):
    model = AuthorDetailsModel
    template_name = 'authors/edit_profile.html'
    form_class = EditProfileForm
    success_url = '/authors/login/'
    success_message = 'Profile edited successfully.'

class DeleteAuthorView(SuccessMessageMixin, View):
    template_name = 'authors/delete_author.html'
    success_message = 'Author deleted'
    model = AuthorDetailsModel

    def get(self, request, id):
        author = AuthorDetailsModel.objects.get(id=id)
        return render(request, self.template_name, {'author': author})
    
    def post(self, request, id):
        author = AuthorDetailsModel.objects.get(id=id)
        author.user.delete()
        author.delete()
        messages.success(request, 'Author Deleted Successfully.')
        return redirect('all-authors')
    
class AuthorProfileView(DetailView):
    template_name = 'authors/view_author.html'
    model = AuthorDetailsModel
    context_object_name = 'author'

class ProfileView(View):
    template_name = 'authors/profile.html'

    def get(self, request):
        return render(request, self.template_name)
    
class AuthorHomePage(View):
    template_name = 'authors/homepage.html'
    
    def get(self, request):
        posts = ArticleModel.objects.filter(author=request.user.id)
        return render(request, self.template_name, {'posts': posts})
    
class AllAuthorsView(TemplateView):
    template_name = 'authors/view_authors.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = AuthorDetailsModel.objects.all()
        return context