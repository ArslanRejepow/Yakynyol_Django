from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Notice
		fields = "__all__"
