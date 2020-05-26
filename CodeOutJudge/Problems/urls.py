from django.urls import path
from . import views

app_name = 'Problems'
urlpatterns = [
    path('' , views.index , name = 'index'),
    path('login/' , views.log_in , name = 'login'),
    path('signup/' , views.sign_up , name = 'signup'),
    path('signup_request/' , views.sign_up_request , name = 'sign_up_request'),
    path('additional_info/' , views.additional_info , name = 'additional_info'),
]