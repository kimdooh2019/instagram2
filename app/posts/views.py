from django.shortcuts import render, redirect

# Create your views here.
from posts.forms import PostCreateForm, CommentCreateForm
from posts.models import Post, PostLike


def post_list_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-pk')
    comment_form = CommentCreateForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/post-list.html', context)


def post_detail_view(request):
    pass


def post_create_view(request):
    if request.method == 'POST':
        text = request.POST['text']
        # image = request.FILES['image']
        # image 여러개 받을 때는
        images = request.FILES.getlist('image')
        post = Post.objects.create(author=request.user, content=text)
        # post.images_set.create(image=image)
        for image in images:
            post.images_set.create(image=image)
        return redirect('posts:post-list')
    else:
        form = PostCreateForm()
        print(form)

    context = {
        'form': form,
    }
    return render(request, 'posts/post-create.html', context)


def post_like_view(request, pk):
    user = request.user
    post = Post.objects.get(pk=pk)
    post_like_qs = PostLike.objects.filter(author=user, post=post)
    # 발견되지 않으면 null이다.(좋아요가 안눌린상태 버튼일때 누르면 return value는 존재하는 값이 나올 것이다
    # 좋아요 눌린 상태일때 버튼 누르면 return postlike 존재한다.
    print(post_like_qs)
    if post_like_qs.exists():
        post_like_qs.delete()
    else:
        PostLike.objects.create(author=user, post=post)
    return redirect('posts:post-list')


def post_comment_view(request, post_pk):

    if request.method == 'POST':
        post = Post.objects.get(pk=post_pk)
        user = request.user
        # comment = request.POST['comment']
        # postcomment = post.postcomment_set.create(author=user, content=comment)
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            form.save(post=post, author=user)
        return redirect('posts:post-list')
