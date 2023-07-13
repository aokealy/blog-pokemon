from django.shortcuts import render
from .models import BlogPostModel

# Create your views here.

def core(request):
    blogpost = BlogPostModel.objects.all()
    return render(request, 'blog/core.html', {'blogpost':blogpost})


