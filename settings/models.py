from django.db import models

# Create your models here.


class Settings(models.Model):
    site_name= models.CharField( max_length=50)
    logo= models.ImageField( upload_to='settings/')
    phone= models.CharField( max_length=15)
    email = models.EmailField(max_length=254)
    descraption = models.TextField(max_length=500)
    fb_link =  models.URLField( max_length=200)
    twitter_link =  models.URLField( max_length=200)
    instagram_link =  models.URLField( max_length=200)
    
      
    def __str__(self):
        return self.site_name 
    
    
