from django.contrib import admin
from .models import category, products, rating
# Register your models here.
admin.site.register(category)
admin.site.register(products)
admin.site.register(rating)