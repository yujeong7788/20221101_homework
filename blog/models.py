from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정
    
    def __str__(self):
        return f'[{self.id}] {self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'