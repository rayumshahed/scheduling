from django.db import models

class PersonSchedule(models.Model):
    PeronName = models.CharField(max_length=30)