from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
     path('register/', views.register, name='register'),
     path('account/', views.account, name='account'),
     path('', auth_view.LoginView.as_view(template_name='accounts/login.html'), name='login'),
     path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]