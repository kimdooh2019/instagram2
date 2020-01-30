from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.forms import LoginForm, SignupForm
import requests

User = get_user_model()


def login_view(request):
    # if request.method == 'POST':
    # username = request.POST['username']
    # password = request.POST['password']
    # # email = request.POST['email']
    # # name = request.POST['name']
    #
    # print(username)
    # print(password)
    # user = authenticate(request, username=username, password=password)
    # # user = authenticate( username=username, password=password)
    # # return value = kimdooh request없어도 됨
    # print(user)
    # if user is not None:
    #     login(request, user)
    #     return redirect('index')
    # else:
    #     return redirect('members:login')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:post-list')

    else:
        # 입력했던 데이터 안날려먹으려고 이렇게 로직 구
        form = LoginForm()
    login_base_url = 'https://nid.naver.com/oauth2.0/authorize'
    login_params = {
        'response_type':'code',
        'client_id': 'XgjJDOfau4a3p4w7excG',
        'redirect_uri': 'http://localhost:8000/members/naver-login/',
        'state':'RANDOM_STATE',
    }
    login_url = '{base}?{params}'.format(
        base=login_base_url,
        params='&'.join([f'{key}={value}' for key,value in login_params.items()])
    )
    context = {
        'form': form,
        'login_url':login_url,
    }

    return render(request, 'members/login.html', context)


def signup_view(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # email = request.POST['email']
    # name = request.POST['name']
    #
    # if User.objects.filter(username=username):
    #     return HttpResponse('이미 사용중인 username입니다')
    # if User.objects.filter(email=email):
    #     return HttpResponse('이미 사용중인 email입니다.')
    # user = User.objects.create(
    #     username=username,
    #     password=password,
    #     email=email,
    #     name=name,
    # )
    # login(request, user)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts:post-list')
    else:
        form = SignupForm()
    context = {
        'form': form,
    }
    return render(request, 'members/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('members:login')
