from django.contrib import admin
from django.urls import path, include
from .views import FoodListView

urlpatterns = [
    path('api/v1/foods/', FoodListView.as_view())
]