from django.urls import path
from .views import all_content, add_notice, addNotice, onumchilik, sowda, okuw, habar

urlpatterns = [
	path('', all_content, name='notices'),
	path('<int:page>', all_content, name='notices_by_page'),
	path('add_notice', add_notice, name='add_notice'),
	path('add_notice_view', addNotice, name='add_notice_view'),
	path('onumchilik', onumchilik, name='onumchilik'),
	path('sowda', sowda, name='sowda'),
	path('okuw', okuw, name='okuw'),
	path('habar', habar, name='habar'),
]