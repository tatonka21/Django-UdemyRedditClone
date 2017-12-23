from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":

        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html', {'error': 'eUsername has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                login(request,user)
                return render(request, 'accounts/signup.html')

        else:
            return render(request,'accounts/signup.html', {'error': 'Passwords didn\'t match.'})


    else:
        return render(request, 'accounts/signup.html')

def loginview(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if 'next' in request.POST:
                if request.POST['next'] is not None:
                    return redirect(request.POST['next'])
            return render(request,'accounts/login.html', {'error': 'Login Success!'})
        else:
            return render(request,'accounts/login.html', {'error': 'The Username and Password didn\'t match'})
    else:
        return render(request, 'accounts/login.html')
