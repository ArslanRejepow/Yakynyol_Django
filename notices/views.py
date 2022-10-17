from django.shortcuts import render, redirect
from .models import Notice, Comment_for_Notice, Favorites_Notice
from .forms import NoticeForm
from users.models import User
from django.core.paginator import Paginator
# Create your views here.

def add_comment(request, uri):
	if request.method == "POST":
		if request.POST.get('comment_id'): replied_comment = request.POST.get('comment_id')
		try:
		    comment_object = Comment_for_Notice.objects.get(pk=replied_comment)
		except:
		    comment_object = None
		
		user_ = User.objects.get(pk = request.user.pk)
		content = Notice.objects.get(pk =request.POST.get('content_id'))

		comment = Comment_for_Notice(body = request.POST.get('comment'), user = user_, content= content, reply_to=comment_object)
		comment.save()
	return redirect(uri)

def all_content(request, page=1):
	objects_list = Notice.objects.filter(is_active=True)
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'content' : objects,
		'paginator' : paginator
	}
	
	return render(request, "notice/all.html", context = context)	

def add_notice(request):
	return render(request, 'notice/add_notice.html')

def addNotice(request):
    context ={}

    # create object of form
    tempdict = request.POST.copy()
    user_ = User.objects.get(pk = request.user.pk)
    print(user_)
    tempdict['user'] = user_
    request.POST = tempdict  # this is the added line
    print(request.POST)
    form = NoticeForm(request.POST or None, request.FILES or None)
    print(form.is_valid())
    print(form)
    # print(form)
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect('notices')
    context['form']= form
    return render(request, "add_notice.html", context)

def onumchilik(request, page=1):
	objects_list = Notice.objects.filter(is_active=True, category = 'onumchilik')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'content' : objects,
		'paginator' : paginator
	}
	
	return render(request, "notice/onumchilik.html", context = context)	

def sowda(request, page=1):
	objects_list = Notice.objects.filter(is_active=True, category = 'sowda')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'content' : objects,
		'paginator' : paginator
	}
	
	return render(request, "notice/sowda.html", context = context)	

def okuw(request, page=1):
	objects_list = Notice.objects.filter(is_active=True, category = 'okuw')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'content' : objects,
		'paginator' : paginator
	}
	
	return render(request, "notice/okuw.html", context = context)	

def habar(request, page=1):
	objects_list = Notice.objects.filter(is_active=True, category = 'habar')
	paginator = Paginator(objects_list, 10)

	objects = paginator.get_page(page)

	context = {
		'content' : objects,
		'paginator' : paginator
	}
	
	return render(request, "notice/habar.html", context = context)	

def delete_comment(request, pk, uri):
	instance = Comment_for_Notice.objects.get(pk=pk)
	instance.delete()


	return redirect(uri)

def add_to_favorites(request, pk, uri):
	user_ = User.objects.get(pk = request.user.pk)
	notice_ = Notice.objects.get(pk =pk)

	notice = Favorites_Notice(notice = notice_, user = user_)
	notice.save()
	return redirect(uri)

def favorites_notice(request):
	
	return render(request, 'notice/favorites.html')