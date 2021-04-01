from django.urls import path
from . import views

urlpatterns = [
    path('available/',					views.available,		name='available'),
    path('available/<int:id>',			views.available,		name='available'),
    path('purchased/',			views.purchased,		name='purchased'),
    path('issued/',			views.issued_coupons,		name='issued'),
    path('issued/<int:pk>',			views.issued_coupons,		name='issued'),
    # path('dashboard/',			views.dashboard,		name='dashboard'),
    # path('issued/<int:pk>',			views.issued_coupons,		name='issued'),
    # path('test1/',            views.test1,     name='test1'),
]
