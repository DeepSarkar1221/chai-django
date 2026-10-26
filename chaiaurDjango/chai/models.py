from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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


##One to Many Function
class ChairReview(models.Model):

    CHAI_RATINGS=[
        (1,"Very Poor"),
        (2,"Poor"),
        (3,"Avrage"),
        (4,"Good"),
        (5,"Excellent"),
    ]

    chai=models.ForeignKey(Chaivariety,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(max_length=1,choices=CHAI_RATINGS)
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.user.username} review for {self.chai.image}'


# Many to Many

class Store(models.Model):
    name=models.TextField(max_length=100)
    location=models.TextField(max_length=100)
    chai_varities= models.ManyToManyField(Chaivariety,related_name='stores')

    def __str__(self):
        return self.name


