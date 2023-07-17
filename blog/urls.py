from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.core, name='core'),
    path('blog_detail/<int:pk>/', views.blog_detail, name='blog-detail'),
    path('blog_edit/<int:pk>/', views.blog_edit, name='blog-edit'),
    
]