# from django.contrib.auth.models import User
from rest_framework import serializers
from onpick.models import Category

# onpick목록(카테고리)
class OnpickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'