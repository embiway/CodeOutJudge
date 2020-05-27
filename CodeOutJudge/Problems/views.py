from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .models import Profile , Submission
from django.http import HttpResponse , Http404
from .models import Problem
from django.conf import settings
from django.core.files.storage import FileSystemStorage

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
        return redirect('/')
    
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

def log_out(request):
    logout(request)
    return redirect('/')

def list_problems(request):
    problems = Problem.objects.all()
    profile = Profile.objects.get(user = request.user)
    attempted_problems = profile.problem_set.all()
    context = {'problems' : problems , 'attempted_problems' : attempted_problems}
    return render(request , 'problems/problem_list.html' , context)


def view_problem(request , problem_id):
    try:
        problem = Problem.objects.get(id = problem_id)
        sample_input = problem.inputfile_set.first()
        sample_output = sample_input.output_file

        file = open(sample_input.file_content.path , 'r')
        sample_input_text = file.read()
        file.close()
        

        file = open(sample_output.file_content.path , 'r')
        sample_output_text = file.read()
        file.close()

        context = { 'problem' : problem ,
                    'sample_input' : sample_input_text , 
                    'sample_output' : sample_output_text }
        return render(request , 'problems/view_problem.html' , context)
    except:
        raise Http404('Problem Not Found')


def run_code(request , problem_id):
    problem = Problem.objects.get(id = problem_id)
    problem.submission_set.create(submission = request.FILES.get('code'))
    code = problem.submission_set.last()
    file_content = open(code.submission.path , 'r')
    code_content = file_content.read()
    return HttpResponse(code_content)