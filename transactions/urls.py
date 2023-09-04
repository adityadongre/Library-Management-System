from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.transaction_list, name='transaction_list'),
    path('issue/', views.issue_book, name='issue_book'),
    path('return/', views.return_book, name='return_book'),
]
