from django.contrib import admin
from .models import Item, Shop, Stock

admin.site.register(Item)
admin.site.register(Shop)
admin.site.register(Stock)