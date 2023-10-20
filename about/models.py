from django.db import models

# Create your models here.



class About(models.Models):
    what_we_do= models.TextField(max_length=1000)
    our_mission= models.TextField(max_length=1000)
    our_goals= models.TextField(max_length=1000)
    image=models.ImageField( upload_to='about/')
    
    
    def __str__(self):
        return str(self.id)
    
    
    
class FQA(models.Models):
    title= models.CharField( max_length=250)
    descraption = models.TextField(max_length=1000)
    
    
    def __str__(self):
        return self.title