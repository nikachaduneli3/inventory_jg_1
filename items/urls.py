from rest_framework.routers import SimpleRouter
from .views import ItemViewSet, CategoryViewSet


router = SimpleRouter(use_regex_path=False)
router.register('categories', CategoryViewSet)
router.register('items', ItemViewSet)

urlpatterns = router.urls
