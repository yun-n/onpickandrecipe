from onpick.serializers import commentserializers
from rest_framework import generics, viewsets
from onpick.models import Comment, OnpickYoutube
from django.shortcuts import get_object_or_404


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentserializers.CommentSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        onpick = get_object_or_404(OnpickYoutube, pk=pk)
        serializer.save(onpick=onpick)


