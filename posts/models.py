from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('data published')
    content = models.TextField()
    email = models.EmailField(max_length=200, blank=True)
    url = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
    
