from django.urls import path
from . import views

urlpatterns = [
    path('shared-tasks/', views.SharedTaskList.as_view()),
]
