# models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from users.validators import validate_names

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        # Ensure that the superuser has `is_staff` and `is_superuser` set to True.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # You should set `username` to `None` or a blank value for the superuser,
        # because you are using `email` as the unique identifier.
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    birthdate = models.DateField()
    first_name = models.CharField(max_length=25, validators=[validate_names])
    last_name = models.CharField(max_length=25, validators=[validate_names])

    # Since we're using email as the unique identifier, set USERNAME_FIELD to 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'birthdate']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
