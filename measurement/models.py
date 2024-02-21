from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=350)
    

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete = models.CASCADE)
    measurements = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
