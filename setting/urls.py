from django.urls import path
from .views import login_view, profile, logout_view, choose_lesson


urlpatterns = [
    path('', login_view, name='login'),
    path('profile', profile, name='profile'),
    path('logout', logout_view, name='logout'),
    path('choose_lesson', choose_lesson, name='choose_lesson')
]