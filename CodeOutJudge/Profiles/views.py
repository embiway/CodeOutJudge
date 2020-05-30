from django.shortcuts import render , redirect
from Problems.models import Profile , Problem , Blogs , Submission
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.
def view_profile(request , profile_id):
    try:
        profile = Profile.objects.get(id = profile_id)
        problem_count = profile.problem_set.count()
        blogs = profile.creator.all()

        return render(request , 'profiles/display_profile.html' , {
            'profile' : profile,
            'problem_count' : problem_count,
            'blogs' : blogs,
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
    })