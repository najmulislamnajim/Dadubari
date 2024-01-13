from django.db import models

# Create your models here.
class CategoriesModel(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    category_description=models.CharField(max_length=125,blank=True)
    category_image=models.ImageField(upload_to='images/categories',blank=True)
    
    def __str__(self):
        return f'{self.category_name}'