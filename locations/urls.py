from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.food_trucks_nearby),
]
