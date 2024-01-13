from django.urls import path
from . import views 

urlpatterns = [
    path('',views.cart,name='cart'),
    path('<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove/<int:product_id>/',views.remove_cart_item,name='remove_cart_item'),
    path('reduce/<int:product_id>/',views.reduce_cart_item,name='reduce_cart_item'),
]
