# api/serializers.py

from rest_framework import serializers
from .models import Store

class StoreSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Store
        fields = ('key', 'value', 'date_created', 'date_modified')
        
