from django.urls import path
from . import views

app_name = 'Profiles'
urlpatterns = [
    path('view_profile/<int:profile_id>' , views.view_profile , name = 'view_profile'),
    path('find_profile/' , views.find_profile , name = 'find_profile'),
    path('not_found/' , views.display_profile_not_found , name = 'profile_not_found'),
    path('<int:profile_id>/submissions' , views.submissions_display , name = 'submissions'),
    path('<int:profile_id>/blogs/' , views.user_blogs_list , name = 'blog_list'),
    path('<int:blog_id>/display_blog' , views.display_blog , name = 'blog_display'),
    path('<int:profile_id>/user_problems' , views.user_problem , name = 'user_problem'),
    path('blog_form/' , views.blog_form_render , name = 'blog_form'),
    path('save_form/' , views.get_blog , name = 'save_blog'),
    path('comment/<int:blog_id>' , views.add_comment , name = 'add_comment'),
]