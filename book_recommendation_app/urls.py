from django.shortcuts import render
from django.urls import path
from .views import (
    BookCreateAndListAPIView
)

# Create your views here.

urlpatterns = [
    # Book Management
    path('books/', BookCreateAndListAPIView.as_view(), name='add_list_book'),

]