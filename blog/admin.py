from django.contrib import admin
from .models import BlogPostModel

# Register your models here.
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

admin.site.register(BlogPostModel, BlogPostModelAdmin)
