from django.db.models import Prefetch
from .models import FoodCategory, FoodListSerializer, Food
from rest_framework import generics


class FoodListView(generics.ListAPIView):
    queryset = FoodCategory.objects.prefetch_related(
        Prefetch('food', queryset=Food.objects.filter(is_publish=True))
    ).distinct().order_by('id')
    serializer_class = FoodListSerializer


