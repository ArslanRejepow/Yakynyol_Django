from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username','mobile_no']
    list_filter = ('is_active', 'velayat')
    list_display = ['username', 'mobile_no', 'velayat', 'is_active', 'market']

admin.site.register(User,UserAdmin)
admin.site.unregister(Group)