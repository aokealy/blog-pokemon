from django.urls import path
from .import views

urlpatterns = [
    path('blog/', views.core, name='core'),
    
]