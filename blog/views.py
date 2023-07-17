from django.shortcuts import render, redirect
from .models import BlogPostModel
from .forms import BlogPostModelForm

# Create your views here.

def core(request):
    blogpost = BlogPostModel.objects.all()
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
           instance = form.save(commit=False)
           instance.author = request.user
           instance.save()
           return redirect('core')
    else:
        form = BlogPostModelForm()    
    context = {
        'blogpost': blogpost,
        'form': form
    }
    return render(request, 'blog/core.html', context)

def blog_detail(request, pk):
    post = BlogPostModel.objects.get(id=pk)   

    context = {
        'post':post,
        
    }
    return render(request, 'blog/blog_detail.html', context)    
 


