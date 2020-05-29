from django.urls import path
from . import views

app_name = 'Problems'
urlpatterns = [
    path('' , views.index , name = 'index'),
    path('login/' , views.log_in , name = 'login'),
    path('signup/' , views.sign_up , name = 'signup'),
    path('signup_request/' , views.sign_up_request , name = 'sign_up_request'),
    path('additional_info/' , views.additional_info , name = 'additional_info'),
    path('logout/' , views.log_out ,  name = 'logout'),
    path('problems/' , views.list_problems , name = "problems"),
    path('problems/<int:problem_id>/' , views.view_problem , name = 'view_problem'),
    path('<int:problem_id>/run/' , views.run_code , name = "run_code"),
    path('blogs/<int:blog_id>' , views.like_incrementer , name = 'like_incrementer')
]