from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


# from django.db import models
# from django.conf import settings
#
# class Notification(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
#     message = models.TextField()
#     is_read = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     # Optional fields:
#     type = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'order', 'promo', 'system'
#     url = models.URLField(blank=True, null=True)  # Link to relevant page (e.g., order detail)
#
#     def __str__(self):
#         return f"Notification for {self.user.email} - Read: {self.is_read}"
