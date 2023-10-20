from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Property(models.Models):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')  
    price=models.IntegerField(default=0)
    description=models.CharField(max_length=10000)
    place=models.ForeignKey("Place",related_name='property', verbose_name=(""), on_delete=models.CASCADE)
    catagory=models.ForeignKey("Category",related_name='category', verbose_name=(""), on_delete=models.CASCADE)
    created_at= models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    
class PropertyImages(models.Models):
    property = models.ForeignKey(Property, related_name='Property_image', on_delete=models.CASCADE)
    image= models.ImageField(upload_to='propertyimages/' )
    
    def __str__(self):
        return str(self.name)
    
class Prace(models.Models):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='places/' )
    
    
    def __str__(self):
        return str(self.name)
    
class Category(models.Models):
    models.CharField(max_length=50)
    
    
    def __str__(self):
        return str(self.name)
    
    
class PropertyReview(models.Models):
    author= models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rate= models.IntegerField(default=0)
    feedback=models.TextField(max_length=500)
    created_at= models.DateTimeField(default=timezone.now)
    
    
    
    def __str__(self):
        return str(self.property)
    
    
COUNT=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    
)
class PropertyBook(models.Models):
    user= models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    date_from= models.models.DateField(default=timezone.now)
    date_to= models.models.DateField(default=timezone.now)
    guest =models.CharField(max_length=2,choices=COUNT)
    children=models.CharField(max_length=2,choices=COUNT)
    
    
    
    def __str__(self):
        return str(self.property)
    