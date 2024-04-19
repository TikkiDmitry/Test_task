from django.shortcuts import render
from .models import FoodCategory, FoodListSerializer, Food
from rest_framework.views import APIView
from rest_framework.response import Response


class FoodListView(APIView):
    def get(self, request):
        published_foods = Food.objects.filter(is_publish=True)
        categories = FoodCategory.objects.filter(food__in=published_foods).distinct()
        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)


