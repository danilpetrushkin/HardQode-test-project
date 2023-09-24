from django.contrib import admin
from .models import Product, Lesson, LessonWatch




class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_link', 'view_duration')

class LessonWatchAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'watch_time', 'is_watched')
    search_fields = ('lesson', 'is_watched')
# Register your models here.

admin.site.register(Product)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonWatch, LessonWatchAdmin)

