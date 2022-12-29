from django.urls import path

from api.views import add_word, adsApi, breakApi, categoryApi, commentForNoticeApi, dialogApi, favoriteApi, lessonApi, marketApi, noticeApi, productApi, textApi, userApi, wordApi

urlpatterns = [
    path('ads', adsApi, name='ads'),
    path('break', breakApi, name='api_break'),
    path('word', wordApi, name='api_word'),
    path('dialog', dialogApi, name='api_dialog'),
    path('text', textApi, name='api_text'),
    path('category', categoryApi, name='api_category'),
    path('market', marketApi, name='api_market'),
    path('product', productApi, name='api_products'),
    path('notice', noticeApi, name='api_notice'),
    path('commentfornotice', commentForNoticeApi, name='api_commentfornotice'),
    path('lesson', lessonApi, name='api_lesson'),
    path('favorite', favoriteApi, name='api_favorite'),
    path('user', userApi, name='api_user'),
    path('add_word', add_word)
]
