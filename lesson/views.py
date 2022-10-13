from django.shortcuts import render, redirect
from .models import Word, Dialog, Text, Comment
from setting.models import Lesson
from users.models import User
from django.template.defaulttags import register


def text(request):
	if request.method == "GET":
		try:
			pk = request.session['lesson']
		except:
			return redirect('choose_lesson')
	if request.method == "POST":
		request.session['lesson'] = pk = request.POST.get('lesson')
	elif request.session['lesson']:
		pk = request.session['lesson']

	objects = Text.objects.filter(lesson = pk)
	lesson = Lesson.objects.get(pk = pk)


	context = {
		'text' : objects,
		'lesson' : lesson
	}
	print(objects)
	return render(request, 'lesson/text.html', context = context)
# Create your views here.

def get_word_context(request):
	if not request.session['lesson']:
		return redirect('settings')

	pk = request.session['lesson']
	words = Word.objects.filter(lesson = pk)
	lesson = Lesson.objects.get(pk = pk)
	comments = lesson.comments.filter(reply_to=None)

	if request.method == "POST":
		if request.POST.get('comment_id'): replied_comment = request.POST.get('comment_id')
		try:
		    comment_object = Comment.objects.get(pk=replied_comment)
		except:
		    comment_object = None
		user_ = User.objects.get(pk = request.user.pk)
		
		comment = Comment(body = request.POST.get('comment'), user = user_, lesson= lesson, reply_to=comment_object)
		comment.save()

	context = {
	 	'words' : words,
	 	'lesson' : lesson,
	 	'comments' : comments
	 }
	return context

def get_dialog_context(request):
	if not request.session['lesson']:
		return redirect('settings')

	pk = request.session['lesson']
	dialogs = Dialog.objects.filter(lesson = pk)
	lesson = Lesson.objects.get(pk = pk)
	comments = lesson.comments.filter(reply_to=None)

	if request.method == "POST":
		if request.POST.get('comment_id'): replied_comment = request.POST.get('comment_id')
		try:
		    comment_object = Comment.objects.get(pk=replied_comment)
		except:
		    comment_object = None
		user_ = User.objects.get(pk = request.user.pk)
		
		comment = Comment(body = request.POST.get('comment'), user = user_, lesson= lesson, reply_to=comment_object)
		comment.save()

	context = {
	 	'dialogs' : dialogs,
	 	'lesson' : lesson,
	 	'comments' : comments
	 }
	return context

def learn_word(request):
	context = get_word_context(request)
	return render(request, 'lesson/learn_word.html', context = context)

def learn_word_audio(request):
	context = get_word_context(request)
	return render(request, 'lesson/learn_word_audio.html', context = context)

def test_word(request):
	context = get_word_context(request)
	return render(request, 'lesson/test_word.html', context = context)

def learn_dialog(request):
	context = get_dialog_context(request)
	return render(request, 'lesson/learn_dialog.html', context = context)

def dialog_audio(request):
	context = get_dialog_context(request)
	return render(request, 'lesson/dialog_audio.html', context = context)

def test_dialog(request):
	context = get_dialog_context(request)
	return render(request, 'lesson/test_dialog.html', context = context)

def dialog_test_another(request):
	context = get_dialog_context(request)
	return render(request, 'lesson/dialog_test_another.html', context = context)

def dialog_test_turkmen(request):
	context = get_dialog_context(request)
	return render(request, 'lesson/dialog_test_turkmen.html', context = context)
