from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Post(TimeStamp):
    title = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return "{}".format(self.title)

