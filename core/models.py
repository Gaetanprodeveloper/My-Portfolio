from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=20,null=True, blank=True)  # Ensure this field exists
    message = models.TextField(null=True, blank=True)  # Ensure this field exists

    def __str__(self):
        return self.email

# Create your models here.
