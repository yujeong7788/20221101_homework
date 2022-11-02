from django.db import models
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    
    hook_text = models.CharField(max_length=100,blank=True)
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d',blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d',blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성 예정
    
    def __str__(self):
        return f'[{self.id}] {self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name) # 디렉토리 빼고 파일명과 확장자를 빼줌, 파일업로드네임에서 찾을거다

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #보통은ㅇ 마지막ㅇ에 있는거 가져오는게 좋음