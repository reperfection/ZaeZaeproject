from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Hashtag
from accounts.models import User
from .forms import PostForm, PostEditForm, CommentForm, HashtagForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    return render(request, 'main.html')

    
#글쓰기 로그인 제한
@login_required(login_url='/login/')
def create(request, post=None):
    context = {}
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            form.save_m2m()
            
            """
            content = request.POST.get('content') # 본문을 content에 저장
            content_list = content.split()
            # 해시태그 생성
            for word in content_list: #word : ex) 오늘 #날씨 #춥다
                if '#' in word: #만약 #이 붙어있으면 tag 객체를 이용하여 저장
                    hashtag = Hashtag()
                    hashtag.name = word
                    hashtag.save()
                    
                    # 방금 생성된 해시태그와 현재 게시글을 관계 지어줌
                    post_ = Post.objects.get(pk=post.pk)
                    post_.hashtags.add(hashtag)
                    # post 과 hashtag의 중개 테이블에 관계를 생성하는 부분
            """
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form':form})
    #context['form'] = form
    #return render(request, 'create.html', {'form':form})
    
def read(request):
    sort = request.GET.get('sort', '')
    if sort == 'date':
        posts = Post.objects.all().order_by('-date')
    elif sort == 'likes':
        posts = Post.objects.all().order_by('-like_count')
    else:
        posts = Post.objects
    return render(request, 'read.html', {'posts':posts, 'sort':sort})

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


def hashtag(request, hashtag = None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message =  '이미 존재하는 태그입니다.'
                return render(request, 'hashtag.html', {'form':form, 'error_mesaage':error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('read')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'hashtag.html', {'form':form})
            
def hashtag_search(request, hashtag=None):
    if request.method == 'POST':
        word = request.POST.get('search') #word 입력받음
        hashtag = Hashtag.objects.filter(name=word)
        post = Post.objects.filter(hashtags__in=hashtag) # __in을 넣지 않으면 검색 결과가 나오지 않음..
        context = {'post':post, 'hashtag':hashtag, 'word':word}
        return render(request, 'search.html', context)
    else:
        return render(request, 'read.html')
    
@login_required(login_url='/login/')
def likes(request, id):
    user = request.user
    like = get_object_or_404(Post, id=id)
    if request.user in like.post_like.all():
        like.post_like.remove(request.user)
        like.like_count -= 1
        like.save()
    else:
        like.post_like.add(user)
        like.like_count += 1
        like.save()
    return redirect('detail', like.id)