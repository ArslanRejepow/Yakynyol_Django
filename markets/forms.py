from django import forms
from .models import Favourite, Product, Service, ServiceFavourite


class ProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"


class ServiceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Service
        fields = "__all__"


class FavouriteForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Favourite
        fields = "__all__"


class FavouriteServiceForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ServiceFavourite
        fields = "__all__"
