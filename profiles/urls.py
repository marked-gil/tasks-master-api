from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<str:id>/', views.ProfileDetails.as_view()),
]
