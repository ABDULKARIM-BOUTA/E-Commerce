from rest_framework import serializers
from configuration.models import Configuration

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['site_name', 'site_description', 'site_logo', 'updated_at']
        read_ony_fields = ['updated_at']