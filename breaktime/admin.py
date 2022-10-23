from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    search_fields = ['body', 'link']
    list_filter = ('category',)
    list_display = ['body','link', 'category', 'image_tag1', 'image_tag2', 'image_tag3', 'created_at']
    readonly_fields = ['image_tag1', 'image_tag2', 'image_tag3']

admin.site.register(Content, ContentAdmin)

# Register your models here.
