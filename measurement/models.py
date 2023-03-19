from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField('Название датчика', max_length=25)
    description = models.CharField('Описание датчика', max_length=50, null=True, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField('Температура помещения')
    measurement_time = models.DateTimeField('Время измерения', auto_now_add=True)
    image = models.ImageField('Снимок датчика', null=True, blank=True)
