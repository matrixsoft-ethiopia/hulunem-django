import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import render, reverse, redirect
from .models import cart, order
from product.models import products
from shop.models import city
from .forms import DetailForm

# Create your views here.

def add_to_cart(request, **kwarg):
    Cart = cart()
    Cart.user = request.user
    Cart.product = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Cart.cart_date = datetime.datetime.now()
    Cart.save()    
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

def cart_detail(request,**kwargs):
    sum = 0
    existing_cart = cart.objects.filter(user = request.user)
    for items in existing_cart:
        sum += items.product.price

    context = {
        'cart_items': existing_cart,
        'cart_total' : sum
    }

    return render(request, 'cart-summary.html', context)


def delete_cart_item(request, item_id):
    item_to_delete = cart.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('cart:cart_summary'))

def checkout(request,**kwargs):
    cities = city.objects.all()
    sum = 0
    existing_cart = cart.objects.filter(user = request.user)
    for items in existing_cart:
        sum += items.product.price
    existing_cart = cart.objects.filter(user = request.user)
    message= ""
    if existing_cart.exists():
        if request.method == 'POST':
            #Get the posted form
                detailform = DetailForm(request.POST)      
                if detailform.is_valid():
                    for cart_items in existing_cart:
                        Order = order()
                        Order.user = cart_items.user
                        Order.product = cart_items.product
                        Order.cart_date = datetime.datetime.now()            
                        Order.location1 = request.POST.get('location1')
                        Order.location2 = request.POST.get('location2')
                        Order.location3 = request.POST.get('location3')
                        Order.phone_number = request.POST.get('phone_number')
                        Order.save()
                    existing_cart.delete()
                    sum=0
                    message = "√ ትእዛዝዎ በተሳካ ሁኔታ ተልኳል"
                else:
                    detailform = DetailForm()
    context = {
        'cart_items': existing_cart,
        'cart_total' : sum,
        'form' : DetailForm(),
        'city' : cities,
        'message' : message
    }
    
    return render(request, 'checkout.html', context)


def order_detail(request,**kwargs):
    sum = 0
    existing_order = order.objects.filter(user = request.user)
    for items in existing_order:
        sum += items.product.price

    context = {
        'order_items': existing_order,
        'order_total' : sum
    }

    return render(request, 'order-given.html', context)


def order_received_detail(request,**kwargs):
    sum = 0
    existing_order = order.objects.all()
    for items in existing_order:
        sum += items.product.price

    context = {
        'order_items': existing_order,
        'order_total' : sum
    }

    return render(request, 'order-received.html', context)



class ProductDetailView(DetailView):
    queryset = order.objects.all()
    context_object_name = 'productdetail'
    template_name = "order-received-detail.html" 