
from . import views
from django.urls import path
from .views import yt_vid, login_user

<<<<<<< Updated upstream


urlpatterns =   [
    path('', views.login_user, name = 'login'),
    path('yt/', views.yt_vid, name = 'yt_vid'),
    path('pswd/', views.password_page, name = 'password'),
  
]  
=======
urlpatterns = [
    path('yt/', yt_vid, name='yt_vid'),
    path('', login_user, name='login'),
]
>>>>>>> Stashed changes
