from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-books/', views.upload_books, name='upload_books'),
    path('my-books/', views.my_books, name='my_books'),
    path('authors-and-sellers/', views.AuthorsAndSellersView.as_view(), name='authors_and_sellers'),
]
