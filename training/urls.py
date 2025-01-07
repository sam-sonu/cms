# training/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.training_list, name='training_list'),
    path('<int:id>/', views.training_detail, name='training_detail'),
    path('<int:id>/check_feedback/', views.check_feedback, name='check_feedback'),
    path('<int:id>/mark_action/<str:action>/', views.mark_action, name='mark_action'),
]