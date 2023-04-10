
from django.urls import path
from . import views



urlpatterns =   [
    path('', views.login_user, name = 'login'),
    path('yt/', views.yt_vid, name = 'yt_vid')
  
]  