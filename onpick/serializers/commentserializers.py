from onpick.models import OnpickYoutube, Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('onpick', 'user', 'comment', 'created_at','reply')
        read_only_fields = ['user']

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind('', self)
        return serializer.data