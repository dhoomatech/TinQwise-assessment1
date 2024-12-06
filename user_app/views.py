from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from book_recommendation_app.serializers import BookSerializer
from django.db.models import Q
from book_recommendation_app.models import Book

from .serializers import UserSerializer,UserPreferenceSerializer
from .models import User,UserPreference


# User Management
class AddUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# User Preferences
class AddUserPreferenceView(APIView):

    def post(self, request, *args, **kwargs):
        """
            Handle POST request to create or update a new object.
        """
        try:
            user = kwargs.get('user_id')
            post_data = {}
            book_id = request.data.get('book')
            user_preference = request.data.get('preference')
            post_data['user'] = user

            obj, created = UserPreference.objects.get_or_create(
                book_id=book_id,
                user_id=user,
                defaults={"preference": user_preference},
            )
            message = f"Action {user_preference}d"
            return Response({"message":message}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, *args, **kwargs):
        user = kwargs.get('user_id')
        try:
            instance = UserPreference.objects.filter(user__id=user)
            instance.delete()
            return Response({"message": "Preferences reset successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except UserPreference.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)


# Book Recommendations
class BookRecommendationView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        
        user = self.kwargs.get('user_id')
        
        # Prioritize books from genres the user has liked.
        liked_genres = UserPreference.objects.filter(
            user__id=user, preference='like'
        ).values_list('book__genre', flat=True)

        # Books the user has already interacted with
        interacted_books = UserPreference.objects.filter(
            user__id=user
        ).values_list('book_id', flat=True)
        
        if not liked_genres:
            # The 5 most recently added books.
            return Book.objects.all().order_by('-id')[:5]

        recommended_books = Book.objects.filter(
            Q(genre__in=liked_genres) & ~Q(id__in=interacted_books)
        )

        # Include one random suggestion outside their preferred genres to add variety
        random_suggestion = Book.objects.exclude(
            genre__in=liked_genres
        ).exclude(id__in=interacted_books).order_by('?')[:1]
        
        if random_suggestion:
            random_suggestion = recommended_books.union(random_suggestion)
        

        return random_suggestion