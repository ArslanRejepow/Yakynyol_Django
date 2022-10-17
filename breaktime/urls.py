from django.urls import path
from .views import all_content, teachers_content, students_content, masters_content, internet_content, jokes_content, search, add_comment, delete_comment_break

urlpatterns = [
	path('', all_content, name='break'),
	path('<int:page>', all_content, name='break_by_page'),
	path('teachers', teachers_content, name='teachers'),
	path('teachers/<int:page>', teachers_content, name='teachers_by_page'),
	path('students', students_content, name='students'),
	path('students/<int:page>', students_content, name='students_by_page'),
	path('masters', masters_content, name='masters'),
	path('masters/<int:page>', masters_content, name='masters_by_page'),
	path('internet', internet_content, name='internet'),
	path('internet/<int:page>', internet_content, name='internet_by_page'),
	path('jokes', jokes_content, name='jokes'),
	path('jokes/<int:page>', jokes_content, name='jokes_by_page'),
	path('search', search, name='search'),
	path('add_comment_break/<str:uri>', add_comment, name='add_comment_break'),
	path('delete_comment_break/<int:pk>/<str:uri>', delete_comment_break, name='delete_comment_break'),
]