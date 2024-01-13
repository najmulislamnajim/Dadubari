from django.db import models
from category.models import CategoriesModel

# Create your models here.
class ProductsModel(models.Model):
    product_name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    product_price=models.DecimalField(default=0,max_digits=12,decimal_places=2)
    product_details=models.TextField(max_length=500,blank=True)
    product_image=models.ImageField(upload_to='images/products',blank=False)
    product_stock=models.IntegerField()
    product_availability=models.BooleanField(default=True)
    product_create_time=models.DateTimeField(auto_now_add=True)
    product_modified_time=models.DateTimeField(auto_now=True)
    product_category=models.ForeignKey(CategoriesModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product_name} - {self.product_category} '