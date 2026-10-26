from django.db import models
from django.utils import timezone

# Create your models here.

class Chaivariety(models.Model):
    CHAI_TYES_CHOICE=[
        ('ML',"Masala"),
        ('GR',"Green"),
        ('BL',"Black"),

    ] #ENUM
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    types=models.CharField(max_length=2,choices=CHAI_TYES_CHOICE)
    description = models.TextField(default="No description available")

    def __str__(self):
        return self.name
