from django.shortcuts import render
from django.urls import path
from .views import (
    AddUserView, RetrieveUserView,AddUserPreferenceView, BookRecommendationView
)

# Create your views here.


urlpatterns = [
    
    # User Management
    path('users/', AddUserView.as_view(), name='add_user'),
    path('users/<int:pk>/', RetrieveUserView.as_view(), name='retrieve_user'),

    # User Preferences
    path('users/<int:user_id>/preferences/', AddUserPreferenceView.as_view(), name='add_delete_preference'),

    # Book Recommendations
    path('users/<int:user_id>/recommendations/', BookRecommendationView.as_view(), name='book_recommendations'),

]