from rest_framework import serializers
from .models import Tax

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = ['pk', 'name', 'rate', 'country', 'state']
        read_only_fields = ['pk']