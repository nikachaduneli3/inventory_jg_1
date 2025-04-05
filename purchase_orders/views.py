from rest_framework.viewsets import  ModelViewSet
from .models import PurchaseOrder, PurchaseOrderItem
from .serializers import PurchaseOrderSerializer, PurchaseOrderItemSerializer
from rest_framework.decorators import action
from rest_framework.response import  Response
from locations.models import LocationItem


class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def validate_order(self, request, pk):
        order = PurchaseOrder.objects.get(pk=pk)
        if order.completed: return Response({'message': 'already validated'}, status=400)

        location = order.location

        for order_item in order.order_items.all():
            item = order_item.item
            location_item, created = LocationItem.objects.get_or_create(item=item, location=location)
            if created:
                location_item.qty = order_item.qty
            else: location_item.qty += order_item.qty

        order.completed = True
        order.save()
        return Response({'message': 'order validated successfully'}, status=200)

class PurchaseOrderItemViewSet(ModelViewSet):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer