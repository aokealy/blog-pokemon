from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Model for Blog Posts
class BlogPostModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Sort by most recent
    class Meta:
        ordering = ('-date',)

    # Display title in admin
    def __str__(self):
        return self.title




