from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    light_intensity = models.FloatField()
    co2_level = models.FloatField()
    pH_value = models.FloatField()

class Thresholds(models.Model):
    soil_moisture = models.IntegerField(default=700)
    temperature = models.FloatField(default=28.0)
    humidity = models.FloatField(default=60.0)
    co2_level = models.FloatField(default=400.0)  # Default value to be set

class ActuatorControl(models.Model):
    vent_open = models.BooleanField(default=False)
    heating_system = models.BooleanField(default=False)
    cooling_fan = models.BooleanField(default=False)
    water_pump = models.BooleanField(default=False)
    humidifier = models.BooleanField(default=False)
