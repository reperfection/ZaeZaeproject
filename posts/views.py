from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from accounts.models import User
from .forms import PostForm, PostEditForm, CommentForm
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
            form.user = request.user
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
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.created_date = timezone.now()
            comment.post = post
            comment.user = request.user
            comment.content = form.cleaned_data['content']
            comment.save()
            return redirect('detail', id)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'post':post, 'form':form})

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


def update_comment(request, commentid, postid):
    post = get_object_or_404(Post, id=postid)
    comment = Comment.objects.get(id=commentid)
    comment_form = CommentForm(instance=comment)
    if request.method == 'POST':
        update_form = CommentForm(request.POST, instance = comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', postid)
    return render(request, 'update_comment.html', {'comment_form':comment_form, 'post':post})

def delete_comment(request, commentid, postid):
    comment = Comment.objects.get(id=commentid)
    comment.delete()
    return redirect('detail', postid)