from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth, messages
from accounts.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


def login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']

        user = auth.authenticate(username=un, password=pw)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged In')
            return redirect('/')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('/')
    return HttpResponse('Invalid access')


def register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        un = request.POST['un']
        em = request.POST['em']
        pw = make_password(request.POST['pw'])
        mb = request.POST['mb']
        ad = request.POST['ad']
        user = User(first_name=fn, last_name=ln, username=un, email=em,
                    password=pw, mobile=mb, address=ad)
        user.save()

        return redirect('home')
    return HttpResponse('Invalid Access')


def logout(request):
    auth.logout(request)
    messages.warning(request, 'You are logged out!')
    return redirect('home')
