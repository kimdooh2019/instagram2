from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
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
    return render(request, 'members/signup.html')
