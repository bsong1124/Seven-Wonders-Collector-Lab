from django.db import models
from django.urls import reverse

# Create your models here.

class Wonder(models.Model):
    name = models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    year_built = models.CharField(max_length=100)

    def __str__(self):
        return f"name: {self.name}, country: {self.country}, year_built: {self.year_built}"
    
    def get_absolute_url(self):
         return reverse('detail', kwargs={'wonder_id': self.id})

