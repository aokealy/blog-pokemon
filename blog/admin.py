from django.contrib import admin
from .models import BlogPostModel, Comment

# Register your models here.
class BlogPostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')

admin.site.register(BlogPostModel, BlogPostModelAdmin)
admin.site.register(Comment)
