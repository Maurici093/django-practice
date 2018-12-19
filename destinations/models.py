from django.db import models
from clients.models import Client # import model client to related with favorite destination
# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    itinerary = models.CharField(max_length=300)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ("id",)

class Favorite(models.Model):
    user = models.ForeignKey(Client, on_delete=models.PROTECT)
    destination = models.ForeignKey(Destination, on_delete= models.PROTECT)
    
    class Meta:
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'

    def __str__(self):
        return '%s %s' % (self.user.name, self.destination.name)
