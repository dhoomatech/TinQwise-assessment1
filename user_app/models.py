from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from book_recommendation_app.models import Book

class UserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        """
            Create and save a User with the given email and password.
        """
        user = User(**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        
        return self.create_user(password, **extra_fields)
    
class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'

    USERNAME_FIELD = 'username'
    
    username = models.CharField(max_length=100,unique=True,)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255
    )
    
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = UserManager()
    contact_number = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=100, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return f"{self.username} {self.email} {self.is_active}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserPreference(models.Model):
    PREFERENCE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    preference = models.CharField(max_length=10, choices=PREFERENCE_CHOICES)

    class Meta:
        unique_together = ('user', 'book')