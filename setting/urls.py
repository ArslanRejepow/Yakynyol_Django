from django.urls import path
from .views import login_view, profile, logout_view, choose_lesson, add_to_favorites, favorites


urlpatterns = [
    path('', login_view, name='login'),
    path('profile', profile, name='profile'),
    path('logout', logout_view, name='logout'),
    path('choose_lesson', choose_lesson, name='choose_lesson'),
    path('add_to_favorites', add_to_favorites, name='add_to_favorites'),
    path('favorites', favorites, name='favorites')
]