from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User,UserPreference

class UserAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'full_name','contact_number', 'is_active')
    # Fields to search for
    search_fields = ('username', 'email', 'full_name')
    # Field used as the identifier for users
    ordering = ('username',)

# Register the User model with the customized UserAdmin
admin.site.register(User, UserAdmin)



class UserPreferenceAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user', 'book', 'preference')
    # Enable search functionality for specific fields
    search_fields = ('user__username', 'book__title')
    # Enable filters for specific fields
    list_filter = ('preference',)

# Register the model with the admin site
admin.site.register(UserPreference, UserPreferenceAdmin)