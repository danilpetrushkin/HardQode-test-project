from .models import Product, Lesson, LessonWatch
from rest_framework import viewsets, permissions, generics
from .serializers import ProductSerializer, LessonSerializer, LessonWatchSerializer



class ProductViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()


class LessonViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        access_lessons = Lesson.objects.filter(products__owner=user).distinct()
        lesson_status = {}
        for lesson in access_lessons:
            try:
                view_status = LessonWatch.objects.get(user=user, lesson=lesson)
                lesson_status[lesson.id] = {
                    'is_watched': view_status.is_watched,
                    'watch_time': view_status.watch_time
                }
            except LessonWatch.DoesNotExist:
                lesson_status[lesson.id] = {
                    'is_watched': False,
                    'watch_time': 0

                }
        for lesson in access_lessons:
            lesson.is_watched = lesson_status[lesson.id]['is_watched']
            lesson.watch_time = lesson_status[lesson.id]['watch_time']
        return access_lessons


class LessonWatchViewSet(generics.ListAPIView):
    queryset = LessonWatch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonWatchSerializer
