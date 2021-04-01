from django.urls import path
from .views import *

urlpatterns = [
    path('resources/',								all_subs,				name='resources'),
    path('resources/add',							create_resource,		name='resources_add'),
    path('reminder/add',							create_reminder,		name='reminder_add'),
    path('subject/<int:id>',						subject_page,			name='subject_page'),
    path('time/',									time,					name='time'),
]
