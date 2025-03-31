from rest_framework.routers import SimpleRouter
from .views import LocationViewSet, LocationItemViewSet

router = SimpleRouter(use_regex_path=False)
router.register('locations', LocationViewSet)
router.register('location_items', LocationItemViewSet)

urlpatterns = router.urls
