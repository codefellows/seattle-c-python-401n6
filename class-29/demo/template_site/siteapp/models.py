from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Thing(models.Model):
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('thing_detail', args=[str(self.id)])