from django.urls import path
from .views import about, about_english, about_russian, about_chinese, about_turkish

urlpatterns = [
	path('',about, name='about'),
	path('about_english/',about_english, name='about_english'),
	path('about_russian',about_russian, name='about_russian'),
	path('about_chinese',about_chinese, name='about_chinese'),
	path('about_turkish',about_turkish, name='about_turkish'),
]