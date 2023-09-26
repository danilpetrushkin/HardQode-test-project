from rest_framework import routers
from .api import ProductViewSet, LessonViewSet, LessonWatchViewSet
from django.urls import path

#Неудавшийся вариант снизу)
# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register('lessons/product/<int:product_id>/', LessonViewSet.as_view(), basename='Lesson')
# router.register(r'lessons-watches', LessonWatchViewSet)
#
# urlpatterns = router.urls

urlpatterns = [
    path('lessons/', LessonViewSet.as_view(), name='lesson'),
    path('products/', ProductViewSet.as_view(), name='products'),
    path('lessonswatch/', LessonWatchViewSet.as_view(), name='lesson_watch')
]
