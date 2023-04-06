
from django.urls import path
from . import views



urlpatterns =   [
    path('', views.render_page),
    path('login/', views.authenciate_view , name = 'login')
    
]  