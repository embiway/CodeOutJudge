from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .models import Profile , Submission , Problem , Blogs
from django.http import HttpResponse , Http404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import IntegrityError
from .languages import language_dict , languages

import requests
import json

#public api key used : Judge0 Api
url = "https://api.judge0.com/submissions/?base64_encoded=false&wait=false"
base_url = "https://api.judge0.com/submissions/"
additional_stuff = "?base64_encoded=false&wait=false"
fields = "&fields=stdout,stderr,status,time,memory"

#The home page which the user sees 
def index(request):
    if request.user.is_authenticated:
        blogs = Blogs.objects.all().order_by('-created_time')
        profile = Profile.objects.get(user = request.user)
        problem_count = profile.problem_set.count()
        return render(request , 'profiles/index.html' , {
            'profile' : profile, 
            'problem_count' : problem_count,
            'blogs' : blogs,
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
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username = username , password = password)
        login(request , user)

        return render(request , 'profiles/additional_info.html')
    except IntegrityError:
        return render(request , 'profiles/sign_up.html' , {
            'error_message' : 'username already taken',
        })

def additional_info(request):
    user = request.user
    bio = request.POST.get('bio')
    birth_date = request.POST.get('birth_date')
    location = request.POST.get('location')
    image = request.FILES.get('image_url')
    blogs = Blogs.objects.all().order_by('-created_time')

    profile = Profile(user = user , bio = bio , birth_date = birth_date , location = location , profile_pic = image)
    profile.save()

    return render(request , 'profiles/index.html' , {
            'profile' : profile,
            'blogs' : blogs,
            'problem_count' : '0',
        })

def log_out(request):
    logout(request)
    return redirect('/')

def like_incrementer(request , blog_id , blog_location):
    blog = Blogs.objects.get(id = blog_id)
    try:
        profile = Profile.objects.get(user = request.user)
        user = blog.likes.get(profile)
        if blog_location == "index":
            return redirect('/')
        else:
            return redirect('/profiles/' + str(blog_id) + '/display_blog')
    except:
        blog.likes.add(profile)
        blog.like_count = blog.likes.count()
        blog.save()
        if blog_location == "index":
            return redirect('/')
        else:
            return redirect('/profiles/' + str(blog_id) + '/display_blog')

def list_problems(request):
    problems = Problem.objects.all()
    profile = Profile.objects.get(user = request.user)
    attempted_problems = profile.problem_set.all()

    #attempted problems : problems for which the user has some submission
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
                    'sample_output' : sample_output_text,
                    'languages' : languages, }
        return render(request , 'problems/view_problem.html' , context)
    except:
        raise Http404('Problem Not Found')


def run_code(request , problem_id):
    if request.method == 'POST' and request.FILES.get('code'):
        language_id = request.POST.get('language_selection')
        profile = Profile.objects.get(user = request.user)
        problem = Problem.objects.get(id = problem_id)
        code = Submission(submission = request.FILES.get('code') , problem = problem , user = profile)
        code.save()
        file_content = open(code.submission.path , 'r')
        code_content = file_content.read()
        
        sample_input = problem.inputfile_set.last()
        sample_output = sample_input.output_file

        file = open(sample_input.file_content.path , 'r')
        input_text = file.read()
        file.close()
        

        file = open(sample_output.file_content.path , 'r')
        output_text = file.read()
        file.close()

        #data for the api , refer to language.py for languages and their ids
        data = {
            "source_code" : code_content,
            "language_id" : language_dict[language_id],
            "stdin" : input_text
        }
        response = requests.post(url , data)
        
        # Two requests are made : First one (with success code 201) is for running the code
        # Second one is to get the result
        if response.status_code == 201:
            response_json = response.json()
            verdict = requests.get(base_url + response_json["token"] + additional_stuff + fields)

            if verdict.status_code == 200:
                verdict_response = verdict.json()
                
                while verdict_response["status"]["description"] == "Processing" or verdict_response["status"]["description"] == "In Queue":
                    verdict = requests.get(base_url + response_json["token"] + additional_stuff + fields)
                    verdict_response = verdict.json()
                code.time = verdict_response["time"]
                code.memory = verdict_response["memory"]
                code.status = verdict_response["status"]["description"]
                code.language_used = language_id
                code.save()

                if code.status == "Accepted":
                    profile.problem_set.add(problem)

                codes = Submission.objects.filter(user = profile , problem = problem).order_by('-creation_time')
                return render(request , 'problems/Result.html' , {
                    'codes' : codes,
                })
            else:
                return HttpResponse("sorry the code couldn't be processed")
        else:
            raise Http404('Oops !!! Something went wrong')
    else:
        return redirect('/problems/' + str(problem_id))