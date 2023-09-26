from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=80)
    video_link = models.URLField()
    view_duration = models.IntegerField()


    def __str__(self):
        return self.title


class LessonWatch(models.Model):
    DoesNotExist = None
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.IntegerField(default=0)
    is_watched = models.BooleanField(default=False)
    data_viewed = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if self.watch_time >= 0.8 * self.lesson.view_duration:
            self.is_watched = True
        else:
            self.is_watched = False
        super().save(*args, **kwargs)

# Create your models here.
