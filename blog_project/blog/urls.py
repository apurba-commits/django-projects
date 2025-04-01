from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, post_detail, register, logout_view

urlpatterns = [
    path('', home, name='blog-home'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]