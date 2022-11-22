from django import forms
from .models import Favourite, Product

class ProductForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Product
		fields = "__all__"

class FavouriteForm(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = Favourite
		fields = "__all__"
