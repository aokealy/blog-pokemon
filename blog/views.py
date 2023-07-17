from django.shortcuts import render, redirect
from .models import BlogPostModel
from .forms import BlogPostModelForm, BlogPostUpdateForm, CommentForm

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
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-detail', pk=post.id)
    else:
        comment_form = CommentForm()    
    context = {
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'blog/blog_detail.html', context)  


def blog_edit(request, pk):
    post = BlogPostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = BlogPostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', pk=post.id)
    else:
        form = BlogPostUpdateForm(instance=post)
    
    context = {
        'post':post,
        'form':form,

    }
    return render(request, 'blog/blog_edit.html', context)

def blog_delete(request, pk): 
    post = BlogPostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('core')
    context = {
        'post': post
    }
    return render(request, 'blog/blog_delete.html', context)   

 


