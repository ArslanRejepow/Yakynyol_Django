from django.contrib import admin
from .models import Word, Dialog, Text

class DialogAdmin(admin.ModelAdmin):
    list_display = ['question_another', 'answer_another', 'question_turkmen', 'answer_turkmen', 'description', 'additional1', 'additional2', 'wrong_text', 'lesson']
    list_filter = ['lesson__name']

class WordAdmin(admin.ModelAdmin):
    list_display = ['another_lang', 'turkmen', 'additional1', 'additional2', 'additional3', 'description', 'lesson']
    list_filter = ['lesson__name']

class TextAdmin(admin.ModelAdmin):
    list_display = ['another_lang', 'turkmen', 'image_tag1', 'image_tag2', 'lesson']
    list_filter = ['lesson__name']
    

admin.site.register(Word, WordAdmin)
admin.site.register(Dialog, DialogAdmin)
admin.site.register(Text, TextAdmin)
# Register your models here.
