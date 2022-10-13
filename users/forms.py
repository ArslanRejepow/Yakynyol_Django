from django.contrib.auth.forms import UserCreationForm 
from .models import User


class UserRegisterForm(UserCreationForm):
    fields = ('username', 'mobile_no', 'password1', 'password2', 'velayat')
    class Meta:
        model = User #this is the "YourCustomUser" that you imported at the top of the file  
        fields = ('username','mobile_no', 'password1', 'password2','velayat') #etc etc, other fields you want displayed on the form)