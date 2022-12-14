from django.shortcuts import render
from users.forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import Lesson, Favorites
from notices.models import Notice
from users.models import User
from django.http import HttpResponse

# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    form = UserRegisterForm()
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_up':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                username = form.cleaned_data.get('username')
                return redirect('login')
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
    print('\n'*5, dir(request), '\n'*5)
    return render(request, 'settings/profile.html')


def logout_view(request):
    logout(request)
    return redirect("login")


def choose_lesson(request):
    if request.method == "POST":
        if request.POST.get('type') == '1':
            ALL = Lesson.objects.filter(category=request.POST.get('category'))
            context = {
                'data': ALL
            }
            print(context)
            return render(request, 'settings/select_lesson.html', context=context)
            # print(request.POST.get('category'))
    # ALL = Lessons.objects

    return render(request, 'settings/choose_lesson.html')


def add_to_favorites(request):
    pk = request.GET.get('pk')

    user_ = User.objects.get(pk=request.user.pk)
    lesson_ = Lesson.objects.get(pk=pk)

    favorite = Favorites(user=user_, lesson=lesson_)
    favorite.save()
    print(favorite)
    return HttpResponse(favorite)


def favorites(request):

    return render(request, 'settings/favorites.html')


def delete_notice(request, pk):
    notice = Notice.objects.get(pk=pk)
    notice.delete()

    return redirect('profile')
