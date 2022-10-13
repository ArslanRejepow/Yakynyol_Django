from  django.urls import path
from .views import text, learn_word, learn_word_audio, test_word, learn_dialog, dialog_audio, test_dialog, dialog_test_another, dialog_test_turkmen

urlpatterns = [
	path('', text, name='text'),
	path('learn_word', learn_word, name='learn_word'),
	path('word_audio', learn_word_audio, name='learn_word_audio'),
	path('test_word', test_word, name='test_word'),
	path('learn_dialog', learn_dialog, name='learn_dialog'),
	path('dialog_audio', dialog_audio, name='dialog_audio'),
	path('test_dialog', test_dialog, name='test_dialog'),
	path('dialog_test_another', dialog_test_another, name='dialog_test_another'),
	path('dialog_test_turkmen', dialog_test_turkmen, name='dialog_test_turkmen'),
]