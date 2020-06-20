from django.conf.urls import url
from .views import (
products_view,
product_categories_view,
ProductListView, 
ProductDetailView,
add_product_info_view,

SearchListView,
rate5, rate4, rate3, rate2, rate1,
edit_product
)

app_name = 'product_app'

urlpatterns = [
    url(r'add/',products_view),
    url(r'add_product_info/',add_product_info_view, name='add_product_info'),
    url(r'categories/',product_categories_view),
    url(r'list/(?P<category_id>\d+)/$',ProductListView.as_view(), name = 'product-list'),
    
    url(r'search-results/$',SearchListView.as_view(), name = 'search-results'),
    url(r'detail/(?P<pk>\d+)/',ProductDetailView.as_view(), name ='product-detail'),
    url(r'rate5/(?P<item_id>\d+)/', rate5 , name='rate5'),
    url(r'rate4/(?P<item_id>\d+)/', rate4 , name='rate4'),
    url(r'rate3/(?P<item_id>\d+)/', rate3 , name='rate3'),
    url(r'rate2/(?P<item_id>\d+)/', rate2 , name='rate2'),
    url(r'rate1/(?P<item_id>\d+)/', rate1 , name='rate1'),
    url(r'edit-product/(?P<item_id>\d+)/$',edit_product, name ='edit-product'),
]