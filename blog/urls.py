from django.urls import path
from .import views

urlpatterns = [
    path('', views.core, name='core'),
    path('about/', views.about, name='about'),
]