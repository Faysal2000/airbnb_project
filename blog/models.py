from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Models):
    title=models.CharField( max_length=150)
    tags=TaggableManager()
    image=models.ImageField(upload_to='post/')
    created_at=models.models.DateTimeField(default=timezone.now )
    descraption = models.models.TextField(max_length=1000)
    category=models.ForeignKey('Catogary', related_name='post_category', on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.name
    
    
    
class Category(models.Models):
    name=models.CharField( max_length=50)  
  
  
    def __str__(self):
        return self.name
    