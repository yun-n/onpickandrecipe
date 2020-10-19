from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class LifeViewSet(viewsets.ModelViewSet):
    queryset = Life.objects.all()
    serializer_class = LifeSerializer