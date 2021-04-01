from django.urls import path
from .views import *

urlpatterns = [
    path('slot/',									all_slots,				name='slots'),
    path('slot/<int:pk>/<int:id>',									all_slots,				name='slots-book'),
    path('slot/add',								create_slot,			name='slot_add'),
    # path('time/<int:pk>/<int:id>',					time_sel,				name='time_sel'),
]
