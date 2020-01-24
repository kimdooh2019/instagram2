from django.shortcuts import render


# Create your views here.
def post_list_view(request):
    return render(request, 'posts/post-list.html')


def post_detail_view(request):
    pass


def post_create_view(request):
    pass


def post_like_view(request):
    pass
