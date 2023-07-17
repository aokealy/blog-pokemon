from django.test import TestCase
from .forms import BlogPostModelForm, BlogPostUpdateForm, CommentForm


class TestBlogPostModelForm(TestCase):

    def test_title_name_is_required(self):
        form = BlogPostModelForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')


    def test_description_field_is_not_required(self):
        form = BlogPostModelForm({'title': 'Test Blog'})
        self.assertFalse(form.is_valid())

class TestBlogPostUpdateForm(TestCase):

    def test_title_name_is_required(self):
        form = BlogPostUpdateForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')


    def test_description_field_is_not_required(self):
        form = BlogPostUpdateForm({'title': 'Test Blog'})
        self.assertFalse(form.is_valid())

class TestCommentForm(TestCase):

    def test_title_name_is_required(self):
        form = CommentForm({'title': ''})
        self.assertFalse(form.is_valid())
        


    def test_description_field_is_not_required(self):
        form = CommentForm({'title': 'Test Blog'})
        self.assertFalse(form.is_valid())


 


