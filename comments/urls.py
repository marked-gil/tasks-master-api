from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:id>', views.CommentDetails.as_view()),
]
