from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Define the list display for the user list page in the admin interface
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')

    # Fields to be displayed in the user details page in the admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'birthdate')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # List of fields to display in the form for creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'birthdate', 'is_staff', 'is_superuser'),
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')  # Search by email, first name, or last name
    ordering = ('email',)  # Order by email in the admin interface


admin.site.register(User, CustomUserAdmin)
