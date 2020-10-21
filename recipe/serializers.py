from rest_framework import serializers
from .models import *

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = '__all__'

class TrendCommentSerializer(serializers.ModelSerializer):
    # reply = serializers.SerializerMethodField()

    class Meta:
        model = TrendComment
        fields = '__all__'

#<------------------------------------------------------------>

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class FoodCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = FoodComment
        fields = '__all__'

#<------------------------------------------------------------>

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'

class StyleCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = StyleComment
        fields = '__all__'

#<------------------------------------------------------------> 

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'

class DietCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = DietComment
        fields = '__all__'

#<------------------------------------------------------------>

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class PetCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = PetComment
        fields = '__all__'

#<------------------------------------------------------------>

class LifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Life
        fields = '__all__'

class LifeCommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = LifeComment
        fields = '__all__'


   