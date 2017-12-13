from django.db import models

# Create your models here.

class Topics(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Comments(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment