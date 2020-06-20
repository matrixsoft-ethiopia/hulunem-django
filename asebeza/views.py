import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import asebeza, asebeza_rating, category
from .forms import ProductsForm
from shop.models import shops
from cart.models import cart, order
from tracking.models import searched, browsed
from django.http import HttpResponse


def asebeza_categories_view(request):

    context = {}
    context['shop'] = 0
    if request.user.is_authenticated:
        SHOP = shops.objects.filter(owner=request.user)
        if SHOP:
            context['shop'] = 1

    return render(request, "asebeza_category.html", context)


def asebeza_view(request):
    SHOP = shops.objects.get(owner=request.user)
    message = ""
    if SHOP is not None:
        product_qty = asebeza.objects.filter(shop=SHOP).count()
        if product_qty >= 10:
            message = 'x በነጻ መመዝገብ የሚችሉት እቃ ብዛት 10 ነው። ተጨማሪ እቃዎችን ለመመዝገብ የአባልነት ምዝገባ መመዝገብ ይኖርብዎታል።'
        else:
            if request.method == 'POST':
                # Get the posted form
                productform = ProductsForm(request.POST, request.FILES)
                if productform.is_valid():
                    Products = asebeza()
                    Products.shop = SHOP
                    Products.name = productform.cleaned_data['name']
                    Products.category = category.objects.get(
                        title=request.POST.get('category'))
                    Products.detail_text = productform.cleaned_data['detail_text']
                    Products.price = productform.cleaned_data['price']
                    Products.stock_qty = productform.cleaned_data['stock_qty']
                    Products.mainimage = productform.cleaned_data['mainimage']
                    Products.date_added = datetime.datetime.now()
                    Products.save()
                    message = "√ በተሳካ ሁኔታ መዝግበዋል"
                else:
                    productform = ProductsForm()

    context = {}
    context['form'] = ProductsForm()
    context['message'] = message
    context['product_qty'] = product_qty
    return render(request, 'add-asebeza.html', context)


class AsebezaListView(ListView):
    paginate_by = 30
    queryset = asebeza.objects.all()
    template_name = "asebeza-list.html"

    def get_queryset(self, **kwargs):
        cat = asebeza.objects.filter(
            category=self.kwargs.get('category_id', ""))
        if cat is not None:
            return cat

    def get_context_data(self, **kwargs):
        context = super(AsebezaListView, self).get_context_data(**kwargs)
        context['category'] = category.objects.get(
            id=self.kwargs.get('category_id', ""))
        context['shop'] = 0
        if self.request.user.is_authenticated:
            SHOP = shops.objects.filter(owner=self.request.user)
            if SHOP:
                context['shop'] = 1
        return context

