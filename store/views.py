from django.shortcuts import render,get_object_or_404
from . models import ProductsModel
from category.models import CategoriesModel
from django.core.paginator import Paginator

# Create your views here.
def store(request,category_slug=None):
    if category_slug:
        category=get_object_or_404(CategoriesModel,slug=category_slug)
        products=ProductsModel.objects.filter(product_availability=True,product_category=category)
    else:
        products=ProductsModel.objects.filter(product_availability=True)
    categories=CategoriesModel.objects.all()
    page=request.GET.get('page')
    paginator=Paginator(products,9)
    paged_product=paginator.get_page(page)
    context={'products':paged_product,'categories':categories}
    return render(request,'store.html',context)


def productDetails(request,category_slug,product_slug):
    product=ProductsModel.objects.get(slug=product_slug,product_category__slug=category_slug)
    print(product)
    return render(request,'product_details.html',{'product':product})