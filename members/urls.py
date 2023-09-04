from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.member_list, name='member_list'),
    path('add/', views.add_member, name='add_member'),
    path('<int:member_id>/', views.member_detail, name='member_detail'),
    path('members/', views.member_views, name='members'),
]
