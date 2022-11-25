from django.shortcuts import render, redirect
from .models import Content, Comment_for_Content, Favorites_Content
from users.models import User
from django.core.paginator import Paginator

# Create your views here.

def add_comment(request, uri):
	if request.method == "POST":
		if request.POST.get('comment_id'): replied_comment = request.POST.get('comment_id')
		try:
			comment_object = Comment_for_Content.objects.get(pk=replied_comment)
		except:
			comment_object = None
		user_ = User.objects.get(pk = request.user.pk)
		content = Content.objects.get(pk =request.POST.get('content_id'))

		comment = Comment_for_Content(body = request.POST.get('comment'), user = user_, content= content, reply_to=comment_object)
		comment.save()
	return redirect(uri)


def all_content(request, page=None):
	objects_list = Content.objects.all()
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/all.html", context = context)	

def teachers_content(request, page=1):
	objects_list = Content.objects.filter(category='teachers')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/teachers.html", context = context)	

def students_content(request, page=1):
	objects_list = Content.objects.filter(category='students')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/students.html", context = context)	

def masters_content(request, page=1):
	objects_list = Content.objects.filter(category='masters')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/masters.html", context = context)	

def internet_content(request, page=1):
	objects_list = Content.objects.filter(category='internet')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/internet.html", context = context)

def jokes_content(request, page=1):
	objects_list = Content.objects.filter(category='jokes')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'contents' : objects,
		'paginator' : paginator
	}
	
	return render(request, "break/jokes.html", context = context)

def search(request):
	objects_list = Content.objects.filter(body__icontains=request.GET.get('q'))
	
	context = {
		'contents' : objects_list,
	}
	
	return render(request, "break/search.html", context = context)

def delete_comment_break(request, pk, uri):
	instance = Comment_for_Content.objects.get(pk=pk)
	instance.delete()

	print(uri)

	return redirect(uri)

def add_to_favorites(request, pk, uri):
	user_ = User.objects.get(pk = request.user.pk)
	content_ = Content.objects.get(pk =pk)

	content = Favorites_Content(content = content_, user = user_)
	content.save()
	return redirect(uri)

def favorites(request):

	return render(request, 'break/favorites.html')


