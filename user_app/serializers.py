from rest_framework import serializers
from user_app.models import User,UserPreference

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','contact_number','full_name','profile_picture']

class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreference
        fields = ['id', 'user','book', 'preference']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=UserPreference.objects.all(),
                fields=['user', 'book'],
                message="Duplicate preference not allowed"
            )
        ]
