from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter

class TrendViewSet(viewsets.ModelViewSet):
    queryset = Trend.objects.all()
    serializer_class = TrendSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('trend_title',)
    
class TrendCommentViewSet(viewsets.ModelViewSet):
    queryset = TrendComment.objects.all()
    serializer_class = TrendCommentSerializer

#<---------------------------------------------->

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('food_title',)

class FoodCommentViewSet(viewsets.ModelViewSet):
    queryset = FoodComment.objects.all()
    serializer_class = FoodCommentSerializer

#<---------------------------------------------->

class StyleViewSet(viewsets.ModelViewSet):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('style_title',)

class StyleCommentViewSet(viewsets.ModelViewSet):
    queryset = StyleComment.objects.all()
    serializer_class = StyleCommentSerializer

#<---------------------------------------------->

class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('diet_title',)

class DietCommentViewSet(viewsets.ModelViewSet):
    queryset = DietComment.objects.all()
    serializer_class = DietCommentSerializer

#<---------------------------------------------->

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('pet_title',)

class PetCommentViewSet(viewsets.ModelViewSet):
    queryset = PetComment.objects.all()
    serializer_class = PetCommentSerializer

#<---------------------------------------------->

class LifeViewSet(viewsets.ModelViewSet):
    queryset = Life.objects.all()
    serializer_class = LifeSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('life_title',)

class LifeCommentViewSet(viewsets.ModelViewSet):
    queryset = LifeComment.objects.all()
    serializer_class = LifeCommentSerializer

#<---------------------------------------------->



    