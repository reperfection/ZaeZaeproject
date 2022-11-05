from django.db import models
from accounts.models import User
#from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateTimeField('data published')
    content = models.TextField()
    email = models.EmailField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank = True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)
    post_like = models.ManyToManyField(User, related_name='like_users', blank=True)
    like_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name