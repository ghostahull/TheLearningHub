from django.db import models


class Course(models.Model):
    key = models.IntegerField(blank=False)
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField()
    link = models.CharField(max_length=300, blank=False)
