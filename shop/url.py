from django.conf.urls import url
from .views import shop_view, ShopListView, ShopDetailView, edit_shop

app_name = 'shop'

urlpatterns = [
    url(r'add/$',shop_view, name = 'add'),
    url(r'list/',ShopListView.as_view(), name = 'shops-list'),
    url(r'detail/(?P<pk>\d+)/$',ShopDetailView.as_view(), name ='shop-detail'),
    url(r'edit-shop/(?P<shop_id>\d+)/$',edit_shop, name ='edit-shop'),
]