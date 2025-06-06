from rest_framework import serializers 
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'

class URLSerializerRestricted(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'url', 'shortCode', 'createdAt', 'updatedAt']
