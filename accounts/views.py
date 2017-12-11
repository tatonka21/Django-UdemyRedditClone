from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
    if request.method == "POST":
        return HttpResponse('test')
    else:
        return render(request, 'accounts/signup.html')
