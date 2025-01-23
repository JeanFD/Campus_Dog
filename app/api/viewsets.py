from rest_framework import viewsets
from app.api import serializer
from app import models

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.AnimalSerializer
    queryset = models.Animal.objects.all()