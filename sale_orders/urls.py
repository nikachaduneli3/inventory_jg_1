from rest_framework.routers import SimpleRouter
from .views import SaleOrderViewSet, SaleOrderItemViewSet

router = SimpleRouter(use_regex_path=False)
router.register('orders', SaleOrderViewSet)
router.register('order_items', SaleOrderItemViewSet)

urlpatterns = router.urls
