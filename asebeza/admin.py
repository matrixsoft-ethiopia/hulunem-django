from django.contrib import admin
from .models import  asebeza, asebeza_rating, category
# Register your models here.
admin.site.register(asebeza_rating)
admin.site.register(asebeza)
admin.site.register(category)