from django.db import models

class location (models.Model):
    location_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.location_name
