from rest_framework import routers
from .api import ProductViewSet, LessonViewSet, LessonWatchViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'lessons-watches', LessonWatchViewSet)

urlpatterns = router.urls
