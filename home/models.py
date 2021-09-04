from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    
    def __str__(self):
        return self.name + "- " + self.email