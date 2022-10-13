from django.shortcuts import render
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Lesson


# Create your views here.
def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')
	form = UserRegisterForm()
	if request.method == "POST":
		if request.POST.get('submit') == 'sign_up':
			form = UserRegisterForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data.get('username')
				return redirect('profile') 
		elif request.POST.get('submit') == 'login':
			username = request.POST['username']
			password = request.POST['password']
			form = UserRegisterForm(request.POST)
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('profile')

	return render(request, 'settings/login.html', {'form': form})

def profile(request):
	return render(request, 'settings/profile.html')

def logout_view(request):
	logout(request)
	return redirect("login")

def choose_lesson(request):
	if request.method == "POST":
		if request.POST.get('type') == '1':
			ALL = Lesson.objects.filter(category=request.POST.get('category'))
			context = {
				'data':ALL
			}
			print(context)
			return render(request, 'settings/select_lesson.html', context = context)
			# print(request.POST.get('category'))
	# ALL = Lessons.objects

	return render(request, 'settings/choose_lesson.html')