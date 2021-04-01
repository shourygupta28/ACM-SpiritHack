from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('student-register/', views.sregister, name='sregister'),
    path('teacher-register/', views.tregister, name='tregister'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
