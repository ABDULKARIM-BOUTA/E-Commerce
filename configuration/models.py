from django.db import models

class Configuration(models.Model):
    """ to manage the site settings from the database instead of hardcoding """

    site_name = models.CharField(max_length=100)
    site_description = models.TextField()
    site_logo = models.ImageField(upload_to='configuration/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Site Configuration"
