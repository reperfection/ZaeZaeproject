from ast import Pass
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from accounts.forms import UserCreationForm, EditUserForm
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main')

#마이페이지 로그인 제한
@login_required(login_url='/login/')
def mypage(request):
    user = request.user
    user_profile = User.objects.get(id=user.id)
    return render(request, 'mypage.html', {'user_profile':user_profile})
    

@login_required(login_url='/login/')
def edituser(request):
    user = request.user
    edituser = User.objects.get(id=user.id)
    form = EditUserForm()
    
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES)
        if form.is_valid():
            edituser.userphoto = form.cleaned_data.get('userphoto')
            edituser.age = form.cleaned_data.get('age')
            edituser.introduce = form.cleaned_data.get('introduce')
            edituser.address = form.cleaned_data.get('address')
            edituser.save()
            return redirect('mypage')
        else:
            #메세지 추가할 거면 추가
            return render(request, 'edituser.html', {'form':form})
    else:
        return render(request, 'edituser.html', {'form':form})

@login_required(login_url='/login/')
def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('mypage')
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'passwordchange.html', {'form':form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'passwordchange.html', {'form':form})

def register(request):
    return render(request, 'register.html')