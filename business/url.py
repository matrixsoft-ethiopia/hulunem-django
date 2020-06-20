from django.conf.urls import url
from .views import advert_view,membership_view, sell_view, organizations_view, factory_view, distributer_view, shop_view

app_name = 'business'

urlpatterns = [
url(r'advertisement/', advert_view),
url(r'membership_registration/', membership_view),
url(r'sell_products/', sell_view),
url(r'organizations/', organizations_view),
url(r'factory/', factory_view, name= 'factory'),
url(r'distributer/', factory_view, name= 'distributer'),
url(r'shop/', factory_view, name= 'shop'),
]