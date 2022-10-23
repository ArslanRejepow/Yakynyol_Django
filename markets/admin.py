from django.contrib import admin
from .models import Market, Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'un']
    search_fields = ['name', 'un']

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('date',)
    list_display = ['market', 'name', 'image_tag1', 'image_tag2', 'image_tag3', 'price', 'about', 'date']
    search_fields = ['name', 'about']

class MarketAdmin(admin.ModelAdmin):
    list_filter = ('region', 'reg', 'category', 'date')
    search_fields = ['user__username', 'code', 'phone_number', 'name', 'about']
    list_display = ['user', 'image_tag1', 'image_tag2', 'region', 'reg', 'category', 'code', 'phone_number', 'name', 'warning', 'place', 'date', 'about']

admin.site.register(Market, MarketAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

# Register your models here.
