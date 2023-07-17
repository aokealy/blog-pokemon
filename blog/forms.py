from django import forms 
from .models import BlogPostModel

class BlogPostModelForm(forms.ModelForm): 
    description =  forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = BlogPostModel
        fields = ('title', 'description')

class BlogPostUpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPostModel
        fields = ('title', 'description')        
