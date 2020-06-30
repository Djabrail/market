from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (City, Market, Category, Product)

class MarketAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('city',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','old_price', 'category')
    list_filter = ('category',)

class CategoryMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('name',)
    list_filter = ('market',)

admin.site.register(City)
admin.site.register(Market, MarketAdmin)
admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Product, ProductAdmin)