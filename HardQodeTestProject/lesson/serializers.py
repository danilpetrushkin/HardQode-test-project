from rest_framework import serializers
from .models import Product, Lesson, LessonWatch



class ProductSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'owner', 'owner_name']
    def get_owner_name(self, obj):
        return obj.owner.username


class LessonSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    is_watched = serializers.BooleanField()
    watch_time = serializers.IntegerField()
    class Meta:
        model = Lesson
        fields = ['title', 'video_link', 'view_duration', 'products', 'is_watched', 'watch_time']

class LessonWatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonWatch
        fields = '__all__'