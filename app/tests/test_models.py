from django.test import TestCase
from app.models import Post
# Create your tests here.

class TestPostModel(TestCase):
    
    def setUp(self) -> None:
        self.post = Post.objects.create(name='test_post')
        return super().setUp()

    def test_post_created(self):
        
        self.assertEqual(self.post.name, 'test_post')
        self.assertTrue(isinstance(self.post, Post))
