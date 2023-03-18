from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<str:id>', views.TaskDetails.as_view()),
]
