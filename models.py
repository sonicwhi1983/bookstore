from django.db import models 

class Book(models.Model):
    title = models.CharField(max_length=255) 
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quutity = models.IntegerField() 

    def __str__(self):
        return self.title
 # Create your models here.
