from django.conf.urls import url
from .views import questions_view,comments_view,claims_view

app_name = 'comments'

urlpatterns = [
    url(r'questions/$',questions_view),
    url(r'comments/$',comments_view),
    url(r'claims/$',claims_view),
    ]