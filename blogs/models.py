from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Blog(models.Model):
    """ to include articles, announcements, or content marketing"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    # image = models.ImageField(upload_to='notifications/', blank=True, null=True)
    #
    # def save(self, *args, **kwargs):
        # generate a slug automatically
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title