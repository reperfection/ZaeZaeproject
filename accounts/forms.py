from django import forms
from django.contrib.auth import forms as form
from accounts.models import User

class UserCreationForm(form.UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'age', 'address', 'introduce']
        labels = {
            'username' : '닉네임',
            'password1' : '새 비밀번호 생성',
            'password2' : '비밀번호 재입력',
            'age' : '나이',
            'address' : '주소',
            'introduce' : '내 소개'
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control',        
            "pattern" : "[a-zA-Z0-9]+",
            "title" : "특수문자 , 공백 입력불가 다시 확인해주세요."}),
            'password1' : forms.TextInput(attrs={'class': 'form-control'}),
            'password2' : forms.TextInput(attrs={'class': 'form-control'})
        }

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