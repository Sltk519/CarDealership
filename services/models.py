from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=15,decimal_places=2)

    def __str__(self) -> str:
        return self.name
    

