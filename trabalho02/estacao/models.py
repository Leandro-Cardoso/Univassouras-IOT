from django.db import models

class Data(models.Model):
    humidity = models.FloatField(
        null=True,
        blank=True,
        default=0.0
    )
    temperature = models.FloatField(
        null=True,
        blank=True,
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'> {self.created_at}: {self.temperature}°C, {self.humidity}%'
