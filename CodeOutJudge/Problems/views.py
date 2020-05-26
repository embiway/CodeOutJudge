from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request , 'profiles/index.html' , {
            'user' : request.user,
        })
    
    else:
        return render(request , 'profiles/login.html')


def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request , username = username , password = password)
    if user is not None:
        login(request , user)
        return render(request , 'profiles/index.html')
    
    else:
        return render(request , 'profiles/login.html' , {
            'error_message' : 'username or password incorrect',
        })

def sign_up_request(request):
    return render(request , 'profiles/sign_up.html')

def sign_up(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.create_user(username = username , password = password)
    login(request , user)

    # return HttpResponse('Hello')
    return render(request , 'profiles/additional_info.html')

def additional_info(request):
    user = request.user
    bio = request.POST.get('bio')
    birth_date = request.POST.get('birth_date')
    location = request.POST.get('location')

    profile = Profile(user = user , bio = bio , birth_date = birth_date , location = location)
    profile.save()

    return render(request , 'profiles/index.html' , {
            'user' : request.user,
        })