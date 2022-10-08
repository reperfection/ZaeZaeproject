from xml.dom import ValidationErr
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label = '제목',
        widget=forms.TextInput(),
        error_messages={
            'required' : '글을 작성해주세요.'}
    )

    class Meta:
        model = Post
        fields = ['title', 'email', 'url', 'content', 'image']

class PostEditForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        label = '제목',
        widget=forms.TextInput(
            attrs={'readonly':'readonly'}),
        error_messages={
            'required' : '글을 작성해주세요.'}
    )

    class Meta:
        model = Post
        fields = ['title', 'email', 'url', 'content', 'image']    

class EditUserForm(forms.Form):
    age = forms.IntegerField(
        widget=forms.TextInput(),
    )
    
    introduce = forms.CharField(
        widget=forms.TextInput(),
    )
    
    address = forms.CharField(
        widget=forms.TextInput(),
    )
    
    