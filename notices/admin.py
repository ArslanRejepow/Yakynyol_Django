from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'image_tag', 'link', 'category', 'date', 'isComment', 'is_active']
    list_filter = ['user', 'category', 'is_active']
    search_fields = ['user', 'body', 'link']

admin.site.register(Notice, NoticeAdmin)
# Register your models here.
