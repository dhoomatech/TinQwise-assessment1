from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.


# Book Management
class BookCreateAndListAPIView(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Handle GET requests (List)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Handle POST requests (Create)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)