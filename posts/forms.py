from xml.dom import ValidationErr
from django import forms
from .models import Post, Comment, Hashtag
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
        fields = ['title', 'email', 'url', 'content', 'image', 'hashtags']

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
        fields = ['title', 'email', 'url', 'content', 'image', 'hashtags']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']
