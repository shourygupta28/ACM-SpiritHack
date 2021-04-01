from django.urls import path
from .views import *

urlpatterns = [
    path('project-internships/',					InternshipProjects,	    name='project-internships'),
    path('internship-opportunities/',				Internships,		    name='internship-opportunities'),
    path('post-internship/',						InternshipCreateView,	name='post-internship'),
    path('apply/<int:pk>/',						    apply,		            name='apply-for-internship'),
    path('make-visible/',						    check_internship,		name='make-visible'),
    path('make-visible/<int:pk>/',                  accept,                 name='accept'),
]