from django.contrib import admin
from .models import Left_Ad

class Left_Ad_Admin(admin.ModelAdmin):
    list_display = ['link', 'image_tag']
    readonly_fields = ['image_tag']

admin.site.register(Left_Ad, Left_Ad_Admin)
# Register your models here.
