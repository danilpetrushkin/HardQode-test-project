from .models import Product, Lesson, LessonWatch
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, LessonSerializer, LessonWatchSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonSerializer


class LessonWatchViewSet(viewsets.ModelViewSet):
    queryset = LessonWatch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonWatchSerializer
