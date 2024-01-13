from django.shortcuts import render,redirect
from cart.models import ProductsModel
from . models import CartModel,CartItemsModel

# Create your views here.
def cart_id(request): # session id diye cart id nibo
    cart=request.session.session_key
    
def cart(request):
    session_id=request.session.session_key
    cart_id=CartModel.objects.filter(cart_id=session_id).exists()
    cart_items=None
    total=0
    tax=5
    grand_total=0
    if cart_id:
        cart=cart_id=CartModel.objects.get(cart_id=session_id)
        cart_items=CartItemsModel.objects.filter(cart=cart)
        
        for item in cart_items:
            total+=item.product.product_price*item.quantity    
        tax_value=(total*tax)/100
        grand_total=tax_value+total
        
        context={'cart_items':cart_items,'grand_total':grand_total,'tax':tax,'tax_value':tax_value,'total':total}
    return render(request,'cart.html',context)
    
def add_to_cart(request,product_id):
    product=ProductsModel.objects.get(id=product_id)
    print('product=',product)
    session_id=request.session.session_key
    cart_id=CartModel.objects.filter(cart_id=session_id).exists()
    if cart_id:
        cart_item=CartItemsModel.objects.filter(product=product).exists()
        if cart_item:
            item=CartItemsModel.objects.get(product=product)
            item.quantity+=1
            item.save()
        else:
            cart=CartModel.objects.get(cart_id=session_id)
            item=CartItemsModel.objects.create(
                product=product,
                cart=cart,
                quantity=1,
            )
            item.save()
    else:
        cart=CartModel.objects.create(cart_id=session_id)
        cart.save()
    return redirect('cart')

def remove_cart_item(request,product_id):
    product=ProductsModel.objects.get(id=product_id)
    session_id=request.session.session_key
    cart_id=CartModel.objects.get(cart_id=session_id)
    cart_item=CartItemsModel.objects.get(product=product,cart=cart_id)
    cart_item.delete()       
    return redirect('cart')

def reduce_cart_item(request,product_id):
    product=ProductsModel.objects.get(id=product_id)
    session_id=request.session.session_key
    cart_id=CartModel.objects.get(cart_id=session_id)
    cart_item=CartItemsModel.objects.get(product=product,cart=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()       
    return redirect('cart')