from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.productDetails,name='product_details'),
]
