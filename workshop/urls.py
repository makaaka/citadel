from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name='main'),
    path('home',views.home, name='home'),
    path('register', views.register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('static/Invitation Letter - cyber security.pdf', views.download_file, name='download_file'),
]
