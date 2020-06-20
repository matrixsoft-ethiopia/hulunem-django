from django.conf.urls import url
from .views import homepage, adetera_view, matrix_view

app_name = 'homepage'

urlpatterns = [
url(r'^$', homepage, name='home'),
url(r'adetera',adetera_view, name='adetera'),
url(r'matrixsoftethiopia', matrix_view, name='matrix'),
]