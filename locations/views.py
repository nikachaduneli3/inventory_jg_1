from rest_framework.viewsets import ModelViewSet
from .models import Location, LocationItem
from .serializers import LocationSerializer, LocationItemSerializer

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationItemViewSet(ModelViewSet):
    queryset = LocationItem.objects.all()
    serializer_class = LocationItemSerializer