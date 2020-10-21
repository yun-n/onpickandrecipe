from rest_framework import viewsets, generics
from onpick.models import Category
from onpick.serializers import onpick_serializers

# onpick목록(카테고리) 생성
class OnpickList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = onpick_serializers.OnpickSerializer
# onpick목록(카테고리) 수정,삭제
class OnpickDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = onpick_serializers.OnpickSerializer
    
