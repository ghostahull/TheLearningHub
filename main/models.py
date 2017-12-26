from django.db import models

class Course(models.Model):
    key = models.IntegerField(blank=False)
    title = models.TextField()
    desc = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
