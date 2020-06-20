from django.shortcuts import render

# Create your views here.
def advert_view(request,**kwargs):
    return render(request, 'advert.html')

def membership_view(request,**kwargs):
    return render(request, 'membership.html')

def sell_view(request,**kwargs):
    return render(request, 'sell.html')

def organizations_view(request,**kwargs):
    return render(request, 'organizations.html')
    
def factory_view(request,**kwargs):
    return render(request, 'factory.html')

def distributer_view(request,**kwargs):
    return render(request, 'distributer.html')

def shop_view(request,**kwargs):
    return render(request, 'shop.html')