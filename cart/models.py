from django.db import models
from django.contrib.auth.models import User
from store.models import ProductsModel

# Create your models here.
class CartModel(models.Model):
    cart_id=models.CharField(max_length=250)
    cart_added=models.DateTimeField(auto_now_add=True)
    
class CartItemsModel(models.Model):
    product=models.ForeignKey(ProductsModel,on_delete=models.CASCADE)
    cart=models.ForeignKey(CartModel,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    
    def sub_total(self):
        return self.product.product_price*self.quantity
    
    def __str__(self):
        return str(self.product)
    