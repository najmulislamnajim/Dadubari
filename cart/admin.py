from django.contrib import admin
from . models import CartModel,CartItemsModel

# Register your models here.
admin.site.register(CartModel)
admin.site.register(CartItemsModel)