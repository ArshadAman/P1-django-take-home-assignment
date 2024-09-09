from .models import FoodTruck
from django.db.models import F
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FoodSerializer

def find_nearby_food_trucks(lat, lon, radius=0.01):
    # Radius is a rough value for latitude and longitude difference (~1km is ~0.01 degrees)
    nearby_food_trucks = FoodTruck.objects.filter(
        Latitude__range=(lat - radius, lat + radius),
        Longitude__range=(lon - radius, lon + radius)
    )[:5]  # Get at least 5 trucks
    
    return nearby_food_trucks

@api_view(['GET'])
def food_trucks_nearby(request):
    lat = float(request.GET.get('latitude'))
    lon = float(request.GET.get('longitude'))
    food_trucks = find_nearby_food_trucks(lat, lon)
    serailized_data = FoodSerializer(food_trucks,many=True).data
    return Response(serailized_data)


