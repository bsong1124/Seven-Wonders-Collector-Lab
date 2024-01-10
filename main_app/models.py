from django.db import models

# Create your models here.

class Wonder(models.Model):
    name = models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    year_built = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country}, {self.year_built}"
    
