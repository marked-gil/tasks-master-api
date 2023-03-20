from django.urls import path
from . import views

urlpatterns = [
    path('shared-tasks/', views.SharedTaskList.as_view()),
    path('shared-tasks/<str:id>', views.SharedTaskDetails.as_view()),
]
