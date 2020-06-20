from django.conf.urls import url,include
from .views import login_view, register_view,update_profile, user_page_view, logout_view, order_given, order_received

app_name = 'accounts'

urlpatterns = [
    url(r'login/$',login_view, name='login'),
    url(r'logout/$',logout_view),
    url(r'register/$',register_view),
    url(r'edit-profile/', update_profile, name='edit-profile'),
    url(r'user-page/$',user_page_view),
    url(r'order-given/', order_given, name='order-given'),
    url(r'order-received/', order_received, name='order-received'),

]