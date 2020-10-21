# from django.contrib.auth.models import User
from rest_framework import serializers
from onpick.models import OnpickYoutube, Comment


# onpick 상세
class OnpickviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = OnpickYoutube
        fields = '__all__'
        read_only_fields = ['category']

class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('post','user','comment_date','comment_body')
        
        
    def get_reply(self,instance):
        serializer = self.__class__(instance = reply, many = True)
        serializer.bind('',self)
        return serializer.data
