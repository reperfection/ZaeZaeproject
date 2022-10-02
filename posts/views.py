from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm, PostEditForm
from django.utils import timezone
# Create your views here.
def main(request):
    return render(request, 'main.html')

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