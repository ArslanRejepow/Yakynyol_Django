from django.shortcuts import render

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
