from django.contrib import admin
from .models import Lesson, Favorites

class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'link1', 'link2', 'link3', 'category', 'language']
    list_filter = ('category', 'language', )
    search_fields = ['name']

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Favorites)
# Register your models here.
