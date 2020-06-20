from django.contrib import admin
from .models import comment, question, claim
# Register your models here.

admin.site.register(question)
admin.site.register(comment)
admin.site.register(claim)