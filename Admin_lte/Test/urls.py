
from . import views
from django.urls import path
from .views import yt_vid, login_user




urlpatterns =   [
    path('', views.login_user, name = 'login'),
    path('yt/', views.yt_vid, name = 'yt_vid'),
    path('pswd/', views.forgot_password, name = 'password'),
  

]
