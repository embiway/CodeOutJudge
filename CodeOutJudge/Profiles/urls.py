from django.urls import path
from . import views

app_name = 'Profiles'
urlpatterns = [
    path('view_profile/<int:profile_id>' , views.view_profile , name = 'view_profile'),
    path('find_profile/' , views.find_profile , name = 'find_profile'),
    path('not_found/' , views.display_profile_not_found , name = 'profile_not_found'),
    path('<int:profile_id>/submissions' , views.submissions_display , name = 'submissions')
]