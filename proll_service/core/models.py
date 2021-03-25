from django.conf import settings
from django.db import models
from django.utils import timezone


class Establishment(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Assessment(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True) # TODO: Tirar
    establishment_id = models.ForeignKey(Establishment, on_delete=models.CASCADE, blank=True, null=True)
    room = models.CharField(max_length=200, blank=True, null=True)
    evaluated_items = models.CharField(max_length=800, blank=True, null=True)

    def __str__(self):
        return f'self.establishment_id.name - {self.room}'
