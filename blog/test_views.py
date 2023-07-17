from django.test import TestCase, Client
from .models import BlogPostModel
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_core_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'partials/index.html')

    def test_blog_edit_GET(self):
        client = Client()  
        response = self.client.get(f'blog-edit')
        self.assertEquals(response.status_code, 1000)
        self.assertTemplateUsed(render, 'blog/blog_edit.html')

    def test_blog_delete_GET(self):
        client = Client()  
        response = self.client.get(f'blog-delete/{post.id}')
        self.assertEquals(response.status_code, 1000)
        self.assertTemplateUsed(render, '/blog/blog_delete.html')

    
    
    

   



   