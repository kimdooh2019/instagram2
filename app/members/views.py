from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']

        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        # user = authenticate( username=username, password=password)
        # return value = kimdooh request없어도 됨
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('members:login')

    else:

        return render(request, 'members/login.html')


def signup_view(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    name = request.POST['name']

    if User.objects.filter(username=username):
        return HttpResponse('이미 사용중인 username입니다')
    if User.objects.filter(email=email):
        return HttpResponse('이미 사용중인 email입니다.')
    user = User.objects.create(
        username=username,
        password=password,
        email=email,
        name=name,
    )
    login(request, user)

    return redirect('posts:post-list')


def logout_view(request):
    logout(request)
    return redirect('members:login')
