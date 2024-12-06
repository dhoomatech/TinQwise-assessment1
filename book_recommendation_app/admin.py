from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Specify fields to display in the admin list view
    list_display = ('title', 'author', 'genre', 'published_date')
    # Enable search functionality for specific fields
    search_fields = ('title', 'author', 'genre')
    # Enable filters for specific fields
    list_filter = ('genre', 'published_date')
    # Add fieldsets for detailed form view
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'genre')
        }),
        ('Publication Details', {
            'fields': ('published_date',),
        }),
    )

# Register the model with the admin site
admin.site.register(Book, BookAdmin)