from rest_framework.viewsets import  ModelViewSet
from .models import SaleOrder, SaleOrderItem
from .serializers import SaleOrderSerializer, SaleOrderItemSerializer
from rest_framework.decorators import action
from rest_framework.response import  Response

class SaleOrderViewSet(ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    @action(detail=True, methods=['post'])
    def validate_order(self, request, pk):
        order = SaleOrder.objects.get(pk=pk)
        if order.completed: return Response({'message': 'already validated'}, status=400)

        for order_item in order.order_items.all():
            item = order_item.item
            item.stock_qty += order_item.qty
            item.save()
        order.completed = True
        order.save()
        return Response({'message': 'order validated successfully'}, status=200)

class SaleOrderItemViewSet(ModelViewSet):
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer