from django.urls import path, include
from .views import onpick_views, onpickview_views

urlpatterns = [
    path('category/', onpick_views.OnpickList.as_view()), #카테고리 전체
    path('category/<int:pk>/', onpick_views.OnpickDetail.as_view()), #카테고리 상세
    path('category/<int:pk>/onpickyoutube/', onpickview_views.OnpickviewList.as_view()), #카테고리별 onpick 전체
    path('onpickyoutube/<int:pk>/', onpickview_views.OnpickviewDetail.as_view()), #onpick 상세
]