from rest_framework.routers import SimpleRouter
from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet

router = SimpleRouter(use_regex_path=False)
router.register('orders', PurchaseOrderViewSet)
router.register('order_items', PurchaseOrderItemViewSet)

urlpatterns = router.urls
