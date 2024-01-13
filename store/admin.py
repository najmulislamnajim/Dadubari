from django.contrib import admin
from . models import ProductsModel

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=['product_name','product_category', 'product_price','product_stock','product_availability','product_create_time','product_modified_time']
    
admin.site.register(ProductsModel,ProductsModelAdmin)