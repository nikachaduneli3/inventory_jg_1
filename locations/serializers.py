from rest_framework import serializers
from .models import Location, LocationItem


class LocationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationItem
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    location_items = LocationItemSerializer(many=True, read_only=True)
    class Meta:
        model = Location
        fields = '__all__'
