# from django.contrib.auth.models import User
from rest_framework import serializers
from onpick.models import OnpickYoutube

# onpick 상세
class OnpickviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnpickYoutube
        fields = '__all__'
        read_only_fields = ['category']