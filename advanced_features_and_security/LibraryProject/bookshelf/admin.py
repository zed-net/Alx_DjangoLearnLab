from django.contrib import admin
from .models import Book

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'publication_year')
    
    list_filter = ('author', 'publication_year')
    
    search_fields = ('title', 'author')





class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_superuser"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
