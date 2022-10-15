from django.shortcuts import render
from .models import Left_Ad
from django.core import serializers
from django.http import JsonResponse

# Create your views here.

def about(request):
	return render(request, 'base/about.html')

def about_english(request):
	return render(request, 'base/about_english.html')

def about_russian(request):
	return render(request, 'base/about_russian.html')

def about_chinese(request):
	return render(request, 'base/about_chinese.html')

def about_turkish(request):
	return render(request, 'base/about_turkish.html')


def get_left_ads(request):
	data = Left_Ad.objects.all()
	return JsonResponse([item.serialize() for item in data], safe=False)