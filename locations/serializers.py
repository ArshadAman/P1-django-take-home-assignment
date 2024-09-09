from rest_framework.serializers import ModelSerializer
from .models import FoodTruck
class FoodSerializer(ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = "__all__"