from django.shortcuts import render
from .models import BlogPostModel
from .forms import BlogPostModelForm

# Create your views here.

def core(request):
    blogpost = BlogPostModel.objects.all()
    form = BlogPostModelForm()    
    context = {
        'blogpost': blogpost,
        'form': form
    }
    return render(request, 'blog/core.html', context)


