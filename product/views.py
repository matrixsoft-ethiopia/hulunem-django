import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import products, category, rating
from .forms import ProductsForm
from shop.models import shops
from cart.models import cart, order
from tracking.models import searched,browsed
from django.http import HttpResponse
# Create your views here.

def product_categories_view(request):
    return render(request, "product-categories.html")

def add_product_info_view(request):
    return render(request, "add_product_info.html")

def products_view(request):
    SHOP = shops.objects.get(owner=request.user)
    message=""
    if SHOP is not None:
        product_qty = products.objects.filter(shop=SHOP).count()
        if product_qty >= 20:
            message = 'x በነጻ መመዝገብ የሚችሉት እቃ ብዛት 20 ነው። ተጨማሪ እቃዎችን ለመመዝገብ የአባልነት ምዝገባ መመዝገብ ይኖርብዎታል።'
        else:
            if request.method == 'POST':
            #Get the posted form
                productform = ProductsForm(request.POST, request.FILES)      
                if productform.is_valid():
                    Products = products()
                    Products.shop = SHOP
                    Products.name = productform.cleaned_data['name']
                    Products.category = category.objects.get(title=request.POST.get('category'))
                    Products.detail_text = productform.cleaned_data['detail_text']
                    Products.price = productform.cleaned_data['price']
                    Products.stock_qty = productform.cleaned_data['stock_qty']
                    Products.mainimage = productform.cleaned_data['mainimage']
                    Products.date_added = datetime.datetime.now()
                    Products.save()
                    message = "√ እቃውን በተሳካ ሁኔታ መዝግበዋል"
                else:
                    productform = ProductsForm()
    
    context = {}
    context['form'] = ProductsForm()
    context['category'] = category.objects.all()
    context['message'] = message
    context['product_qty'] = product_qty
    return render(request, 'add-products.html', context)






class ProductDetailView(DetailView):
    queryset = products.objects.all()
    context_object_name = 'productdetail'
    template_name = "product-detail.html"   

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView,self).get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            Browsed = browsed()
            Browsed.user = self.request.user
            Browsed.product = self.get_object()
            Browsed.date_added = datetime.datetime.now()
            Browsed.save()
            Cart = cart.objects.filter(product = self.get_object().id, user = self.request.user)
            Order = order.objects.filter(product = self.get_object().id, user = self.request.user)
            Rate = rating.objects.filter(products = self.get_object().id, user = self.request.user).first()
            if Rate is not None:
                context['rate'] = Rate.star
            else:
                context['rate'] = 0

            context['current_order_items'] = len(Order)
            context['current_cart_items'] = len(Cart)

        owner = self.get_object().shop.owner
        current_user = self.request.user
        context['owner'] = owner
        context['current_user'] = current_user
        context['shops'] = shops.objects.get(name=self.get_object().shop)
        return context

def rate5(request, **kwarg):
    Rating = rating()
    Rating.user = request.user
    Rating.products = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Rating.star = 5
    Rating.save()        
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

def rate4(request, **kwarg):
    Rating = rating()
    Rating.user = request.user
    Rating.products = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Rating.star = 4
    Rating.save()        
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

def rate3(request, **kwarg):
    Rating = rating()
    Rating.user = request.user
    Rating.products = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Rating.star = 3
    Rating.save()        
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

def rate2(request, **kwarg):
    Rating = rating()
    Rating.user = request.user
    Rating.products = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Rating.star = 2
    Rating.save()        
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

def rate1(request, **kwarg):
    Rating = rating()
    Rating.user = request.user
    Rating.products = products.objects.filter(id=kwarg.get('item_id',"")).first()
    Rating.star = 1
    Rating.save()        
    return redirect(reverse('product:product-detail',kwargs={'pk': kwarg.get('item_id',"")}))

class ProductListView(ListView):
    paginate_by = 12
    queryset = products.objects.all()
    template_name = "product-list.html"

    def get_queryset(self, **kwargs):
        cat = products.objects.filter(category= self.kwargs.get('category_id',""))
        if cat is not None:
            return products.objects.filter(category= self.kwargs.get('category_id',""))
        

    def get_context_data(self, **kwargs):
        context = super(ProductListView,self).get_context_data(**kwargs)
        context['category'] = category.objects.get(id=self.kwargs.get('category_id',""))
        return context





class SearchListView(ListView):
    paginate_by = 12
    model = products     

    def get_template_names(self):
        query =  self.request.GET.get('search-input')
        if query == "":
            template_name = 'home.html'
        else:
            Search = searched()
            Search.user = self.request.user
            Search.search_name = self.request.GET.get('search-input')
            Search.date_added = datetime.datetime.now()
            Search.save()
            template_name = "search-results.html"
        return template_name

    def get_queryset(self):
        query =  self.request.GET.get('search-input')
        object_list = products.objects.filter(name__icontains=query)
        return object_list
        


def edit_product(request, **kwarg):
    update_product = products.objects.get(id=kwarg.get('item_id',""))
    message = ""
    if request.method == 'POST':
        update_product.name = request.POST.get('name')
        update_product.category = category.objects.get(title=request.POST.get('category'))
        update_product.detail_text = request.POST.get('detail_text')
        update_product.price = request.POST.get('price')
        update_product.stock_qty = request.POST.get('stock_qty')
        if request.FILES.get('mainimage') is not None:
            update_product.mainimage = request.FILES.get('mainimage')
        update_product.save()
        message = "√ በተሳካ ሁኔታ ቀይረዋል"
    context = {
        'name' : update_product.name,
        'category2' : update_product.category,
        'detail_text' : update_product.detail_text,
        'price' : update_product.price,
        'stock_qty' : update_product.stock_qty,
        'mainimage' : update_product.mainimage,
        'message' : message,
        'category' : category.objects.all()
    }
    return render(request, 'edit-product.html', context)