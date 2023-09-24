from rest_framework import serializers
from .models import Product, Lesson, LessonWatch


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonWatch
        fields = '__all__'