from django.conf.urls import url
from .views import (
asebeza_view,
asebeza_categories_view,
AsebezaListView
)

app_name = 'asebeza'

urlpatterns = [
    url(r'add/',asebeza_view, name='add'),
    url(r'category/',asebeza_categories_view, name='category'),
    url(r'list/(?P<category_id>\d+)/$',AsebezaListView.as_view(), name = 'asebeza-list'),
]