from django.urls import path
from .views import all_content, add_notice, addNotice, onumchilik, sowda, okuw, habar, delete_comment, add_comment, add_to_favorites, favorites_notice

urlpatterns = [
	path('', all_content, name='notices'),
	path('<int:page>', all_content, name='notices_by_page'),
	path('add_notice', add_notice, name='add_notice'),
	path('add_notice_view', addNotice, name='add_notice_view'),
	path('onumchilik', onumchilik, name='onumchilik'),
	path('sowda', sowda, name='sowda'),
	path('okuw', okuw, name='okuw'),
	path('habar', habar, name='habar'),
	path('delete_comment/<int:pk>/<str:uri>', delete_comment, name='delete_comment'),
	path('add_comment/<str:uri>', add_comment, name='add_comment'),
	path('add_to_favorites/<int:pk>/<str:uri>', add_to_favorites, name='add_to_favorites_notice'),
	path('favorites', favorites_notice, name='favorites_notice')
]