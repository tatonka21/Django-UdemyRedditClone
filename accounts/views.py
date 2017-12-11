from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
    if request.method == "POST":

        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            return render(request, 'accounts/signup.html')
        else:
            return render(request,'accounts/signup.html', {'error': 'Passwords didn\'t match'})


    else:
        return render(request, 'accounts/signup.html')
