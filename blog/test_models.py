from django.test import TestCase
from .models import BlogPostModel


class TestModels(TestCase):

    def test_blogmodels(self):
        blogpostmodel = BlogPostModel.objects.create(title="Test Model")
        self.assertFalse(blogpostmodel)

      