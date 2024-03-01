from django.db import models

# Create your models here.

class Post(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_posts(cls, name):
        return Post.objects.filter(name=name)

    def __str__(self) -> str:
        return str(self.name) 
    