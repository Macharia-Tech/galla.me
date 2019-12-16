from django.db import models

class location (models.Model):
    location_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Category(models.Model):
    name=models.CharField(max_length = 60)

    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
