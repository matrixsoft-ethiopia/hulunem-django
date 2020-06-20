from django.conf.urls import url
from .views import add_to_cart, cart_detail, delete_cart_item, checkout, order_detail, order_received_detail, ProductDetailView

app_name = 'cart'

urlpatterns = [
url(r'add_to_cart/(?P<item_id>\d+)/', add_to_cart, name='add_to_cart'),
url(r'cart_summary/', cart_detail, name='cart_summary'),
url(r'delete_item/(?P<item_id>\d+)/', delete_cart_item, name='delete_item'),
url(r'checkout/', checkout, name='checkout'),
url(r'order_given/', order_detail, name='order-given'),
url(r'order_received/', order_received_detail, name='order-received'),
url(r'order_received_detail/(?P<pk>\d+)/',ProductDetailView.as_view(), name ='order-received-detail'),
]