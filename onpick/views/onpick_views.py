from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from onpick.models import Category
from onpick.serializers import onpick_serializers

# onpick목록(카테고리) 생성
class OnpickList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = onpick_serializers.OnpickSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
    
    filter_backends = [SearchFilter]
    search_fields = ('category_name',)

# onpick목록(카테고리) 수정,삭제
class OnpickDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = onpick_serializers.OnpickSerializer
    
