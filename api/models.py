from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date = models.DateField()
    
    def __str__(self):
        name = self.email.split('@')
        return name[0]


