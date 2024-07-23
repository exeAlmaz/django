from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=6, decimal_places=2)
    datetime = models.DateField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='sensors', on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='image/', default=None)

    def __str__(self):
        return self.temperature
