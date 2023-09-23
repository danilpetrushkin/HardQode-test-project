from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    products = models.ManyToManyField(Product)
    title = models.CharField(max_length=80)
    video_link = models.URLField()
    view_duration = models.IntegerField()


class LessonWatch(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    watch_time = models.IntegerField()
    is_watched = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.watch_time >= 0.8 * self.lesson.view_duration:
            self.is_watched = True
        else:
            self.is_watched = False
        super().save(*args, **kwargs)

# Create your models here.
