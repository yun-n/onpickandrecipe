from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

class TrendCommentViewSet(viewsets.ModelViewSet):
    queryset = TrendComment.objects.all()
    serializer_class = TrendCommentSerializer

#<---------------------------------------------->

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodCommentViewSet(viewsets.ModelViewSet):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentSerializer

#<---------------------------------------------->

class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class StyleCommentViewSet(viewsets.ModelViewSet):
    queryset = StyleComment.objects.all()
    serializer_class = StyleCommentSerializer

#<---------------------------------------------->

class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

class DietCommentViewSet(viewsets.ModelViewSet):
    queryset = DietComment.objects.all()
    serializer_class = DietCommentSerializer

#<---------------------------------------------->

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetCommentViewSet(viewsets.ModelViewSet):
    queryset = PetComment.objects.all()
    serializer_class = PetCommentSerializer

#<---------------------------------------------->

class LifeViewSet(viewsets.ModelViewSet):
    queryset = Life.objects.all()
    serializer_class = LifeSerializer

class LifeCommentViewSet(viewsets.ModelViewSet):
    queryset = LifeComment.objects.all()
    serializer_class = LifeCommentSerializer

#<---------------------------------------------->


 