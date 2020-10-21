from rest_framework import viewsets,  generics
from onpick.models import OnpickYoutube, Category, Comment
from onpick.serializers import onpickview_serializers 
from django.shortcuts import get_object_or_404

#onpick상세 생성
class OnpickviewList(generics.ListCreateAPIView):
    queryset = OnpickYoutube.objects.all()
    serializer_class = onpickview_serializers.OnpickviewSerializer
    pk_url_kwarg = 'category_id'
    
    # category별 필터
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        qs = super().get_queryset()
        qs = qs.filter(category = pk)
        return qs
    #category의 pk값을 가져온다
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        category = get_object_or_404(Category, pk=pk)
        serializer.save(category=category)

#onpick 상세 수정, 삭제
class OnpickviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OnpickYoutube.objects.all()
    serializer_class = onpickview_serializers.OnpickviewSerializer


