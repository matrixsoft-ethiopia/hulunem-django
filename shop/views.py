import datetime
from django.shortcuts import render
from shop.models import shops, city
from product.models import products
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .forms import ShopForm


# Create your views here.
user = get_user_model()


def shop_view(request):
    cities = city.objects.all()
    shop_check = shops.objects.filter(owner=request.user)
    message=""
    x=0
    if shop_check.exists():
        message = 'x በስርዎ ተመዝግቦ የተረጋገጠ ወይም ለመረጋገጥ የሚጠብቅ አንድ ሱቅ አለ። በነጻ መመዝገብ የሚችሉት አንድ ሱቅ ብቻ ሲሆን ተጨማሪ ሱቆችን ለመመዝገብ የአባልነት ምዝገባ ማከናወን ይኖርቦታል። '
    else:
        if request.method == 'POST':
      #Get the posted form
            shopform = ShopForm(request.POST, request.FILES)      
            if shopform.is_valid():
                SHOP = shops()
                SHOP.owner = request.user
                SHOP. enterprise_type = request.POST.get(' enterprise_type')
                SHOP.name = request.POST.get('name')
                SHOP.detail_text = request.POST.get('detail_text')
                SHOP.location1 = request.POST.get('location1')
                SHOP.location2 = request.POST.get('location2')
                SHOP.location3 = request.POST.get('location3')
                SHOP.phone_number = request.POST.get('phone_number')
                SHOP.TIN_number = request.POST.get('TIN_number')
                SHOP.mainimage = request.POST.get('mainimage')
                SHOP.date_added = datetime.datetime.now()
                tin_check = shops.objects.filter(TIN_number=request.POST.get('TIN_number'))
                if tin_check.exists():
                    message = 'x ያስገቡት TIN NO ከዚህ በፊት ተመዝግቦ የተረጋገጠ ወይም ለመረጋገጥ የሚጠብቅ ነው'
                else:
                    SHOP.save()
                    x=1
                    message = '√ ያስገቡትን መረጃ በተሳካ ሁኔታ ልከዋል። የማረጋገጡ ስራ ሲያልቅ መልእክት ይደርስዎታል '
            else:
                shopform = ShopForm()

    context = {}
    context['form'] = ShopForm()
    context['city'] = cities
    context['x'] = x
    context['message'] = message
    return render(request, 'add-shop.html', context)

class ShopListView(ListView):
    paginate_by = 12
    queryset = shops.objects.all()
    template_name = "shop-list.html"



class ShopDetailView(DetailView):
    queryset = shops.objects.all()
    context_object_name = 'shopdetail'
    template_name = "shop-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(ShopDetailView,self).get_context_data(**kwargs)
        filtered_products = products.objects.filter(shop=self.get_object())
        owner = self.get_object().owner
        current_user = self.request.user
        if filtered_products.exists():
            context['products'] = products.objects.filter(shop=self.get_object())
        context['owner'] = owner
        context['current_user'] = current_user
        return context
        
def edit_shop(request, **kwarg):
    update_shop = shops.objects.get(id=kwarg.get('shop_id',""))
    cities = city.objects.all()
    message = ""
    if request.method == 'POST':
        update_shop.enterprise_type = request.POST.get('enterprise_type')
        update_shop.name = request.POST.get('name')
        update_shop.detail_text = request.POST.get('detail_text')
        update_shop.location1 = request.POST.get('location1')
        update_shop.location2 = request.POST.get('location2')
        update_shop.location3 = request.POST.get('location3')
        update_shop.phone_number = request.POST.get('phonenumber')
        update_shop.save()
        message = "√ በተሳካ ሁኔታ ቀይረዋል"
    context = {
        'enterprise_type' : update_shop.enterprise_type,
        'name' : update_shop.name,
        'detail_text' : update_shop.detail_text,
        'location1' : update_shop.location1,
        'location2' : update_shop.location2,
        'location3' : update_shop.location3,
        'phonenumber' : update_shop.phone_number,
        'tin' : update_shop.TIN_number,
        'message' : message,
        'city' : cities
    }
    return render(request, 'edit-shop.html', context)
