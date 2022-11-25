from django.urls import path

from api.views import adsApi, breakApi, categoryApi, commentForNoticeApi, dialogApi, favoriteApi, lessonApi, marketApi, noticeApi, productApi, textApi, userApi, wordApi

urlpatterns = [
    path('ads', adsApi, name='ads'),
    path('break', breakApi, name='break'),
    path('word', wordApi, name='word'),
    path('dialog', dialogApi, name='dialog'),
    path('text', textApi, name='text'),
    path('category', categoryApi, name='category'),
    path('market', marketApi, name='market'),
    path('product', productApi, name='products'),
    path('notice', noticeApi, name='notice'),
    path('commentfornotice', commentForNoticeApi, name='commentfornotice'),
    path('lesson', lessonApi, name='lesson'),
    path('favorite', favoriteApi, name='favorite'),
    path('user', userApi, name='user'),
]