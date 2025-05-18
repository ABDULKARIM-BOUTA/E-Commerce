from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
    """  customer support for collecting inquiries, feedback, or support requests from users or visitors"""

    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    # subject = models.CharField(max_length=100)
    # is_resolved = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact') # used if user is logged in

    def __str__(self):
        return f"{self.name} - {self.subject}"

class FAQ(models.Model):
    questions = models.TextField()
    answers = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
