from django import forms
from django.contrib.auth import forms as form
from accounts.models import User

class UserCreationForm(form.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'address', 'introduce']


class EditUserForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'address', 'introduce', 'userphoto']

    age = forms.IntegerField(
        required=False,
        widget=forms.TextInput(),
    )
    
    introduce = forms.CharField(
        required=False,
        widget=forms.TextInput(),
    )
    
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(),
    )
    
    userphoto = forms.ImageField(required=False)