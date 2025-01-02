from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import login, authenticate
from .forms import CustomUserChangeForm, CustomUserCreationForm, UploadedFileForm
from .models import UploadedFile, CustomUser
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'user/register.html', {'form': form})

class CustomLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, "Please enter a correct username and password. Note that both fields may be case-sensitive.")
        return render(request, 'user/login.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')

@login_required
def upload_books(request):
    if request.method == 'POST':
        form = UploadedFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            form.save()
            return redirect('my_books')
    else:
        form = UploadedFileForm()
    return render(request, 'user/upload_books.html', {'form': form})

@login_required
def my_books(request):
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'user/my_books.html', {'uploaded_files': uploaded_files})

class AuthorsAndSellersView(ListView):
    model = CustomUser
    template_name = 'user/authors_and_sellers.html'
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.filter(public_visibility=True)
