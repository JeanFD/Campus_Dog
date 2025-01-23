from rest_framework import serializers
from app import models

class AnimalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Animal
        fields = '__all__'