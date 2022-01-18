from django.shortcuts import render , redirect
from Problems.models import Profile , Problem , Blogs , Submission
from django.http import Http404 , HttpResponse
from django.contrib.auth.models import User
from .forms import BlogForm , CommentForm
from django.forms import ModelForm
from django.utils import timezone

# Create your views here.
def view_profile(request , profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
        problem_count = profile.problem_set.count()

        return render(request , 'profiles/display_profile.html' , {
            'profile' : profile,
            'problem_count' : problem_count,
            'profile': profile,
        })

    except:
        raise Http404('Profile Not Found')

def find_profile(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST.get('search'))
            profile = Profile.objects.get(user = user)

            return redirect('/profiles/view_profile/' + str(profile.id))
        
        except:
            return redirect('/profiles/not_found')
        
    else:
        raise Http404('Something went Wrong')

def display_profile_not_found(request):
    return render(request , 'profiles/profile_not_found.html')


def submissions_display(request , profile_id):
    profile = Profile.objects.get(id = profile_id)
    submissions = profile.submission_set.filter(user = profile).order_by('-creation_time')

    return render(request , 'problems/submissions.html' , {
        'codes' : submissions,
        'profile' : profile,
    })


def user_blogs_list(request , profile_id):
    profile = Profile.objects.get(id = profile_id)
    blogs = profile.creator.all().order_by('-created_time')

    return render(request , 'profiles/blog_list.html' , {
        'blogs' : blogs,
        'profile' : profile,
    })

def display_blog(request , blog_id):
    try:
        profile = Profile.objects.get(user = request.user)
        blog = Blogs.objects.get(id = blog_id)
        comments = blog.comments_set.all().order_by('-created_time')
        comment = CommentForm()

        return render(request , 'profiles/blog_display.html' , {
            'blog' : blog,
            'comments' : comments,
            'form' : comment,
            'profile' : profile,
        })
    except:
        raise Http404('Something went Wrong!!!!')

def user_problem(request , profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
        problems = profile.problem_set.all()
        attempted_problems = Profile.objects.get(user = request.user).problem_set.all()

        return render(request, 'profiles/user_solved_problems.html' , {
            'problems' : problems,
            'attempted_problems' : attempted_problems,
            'profile' : profile,
        })
    except:
        raise Http404('Something Went Wrong')


def blog_form_render(request):
    profile = Profile.objects.get(user = request.user)
    form = BlogForm()
    return render(request , 'profiles/blog_form.html' , {
        'form' : form,
        'profile': profile
    })


def get_blog(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':    
        blog_form = BlogForm(request.POST)

        if blog_form.is_valid():
            blog = blog_form.save(commit = False)
            profile = Profile.objects.get(user = request.user)
            blog.user = profile
            blog.created_time = timezone.now()
            blog.save()
            return redirect('/')
    
    else:
        blog = BlogForm()
    
    return render(request , 'profiles/blog_form.html' , {
        'profile' : profile
    })


def add_comment(request , blog_id):
    if request.method == 'POST':
        comment_instance = CommentForm(request.POST)

        if comment_instance.is_valid():
            profile = Profile.objects.get(user = request.user)
            blog = Blogs.objects.get(id = blog_id)

            comment = comment_instance.save(commit = False)
            comment.user = profile
            comment.blog = blog
            comment.created_time = timezone.now()
            comment.save()
        
        
    return redirect('/profiles/' + str(blog_id) + '/display_blog')
    
        

