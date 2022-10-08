from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from accounts.models import User
from .forms import PostForm, PostEditForm, EditUserForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    return render(request, 'main.html')

#글쓰기 로그인 제한
@login_required(login_url='/login/')
def create(request):
    context = {}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.date = timezone.now()
            form.save()
            return redirect('read')

    else:
        form = PostForm()
    context['form'] = form
    return render(request, 'create.html', {'form':form})
    
def read(request):
    posts = Post.objects
    return render(request, 'read.html', {'posts':posts})

def detail(request, id):
    posts = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'posts':posts})

def edit(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')

    else:
        form = PostEditForm(instance=post)
        return render(request, 'edit.html', {'form':form, 'post':post})
    
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('read') 

#마이페이지 로그인 제한
@login_required(login_url='/login/')
def mypage(request):
    user = request.user
    user_mypage = User.objects.get(id=user.id)
    return render(request, 'mypage.html')
    
    
@login_required(login_url='/login/')
def edituser(request):
    user = request.user
    edituser = User.objects.get(id=user.id)
    form = EditUserForm()
    
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES)
        if form.is_valid():
            edituser.age = form.cleaned_data.get('age')
            edituser.introduce = form.cleaned_data.get('introduce')
            edituser.address = form.cleaned_data.get('address')
            edituser.save()
            return redirect('mypage')
        else:
            #메세지 추가할 거면 추가
            return render(request, 'edituser.html', {'form':form})
    else:
        return render(request, 'edituser.html', {'form':form}, {'edituser':edituser})