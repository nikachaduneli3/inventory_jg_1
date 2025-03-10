from rest_framework.viewsets import  ModelViewSet
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer

class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer