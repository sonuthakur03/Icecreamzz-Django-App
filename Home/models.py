from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class CustomOrder(models.Model):
    flavor = models.CharField(max_length=100)
    toppings = models.EmailField()
    quantity = models.CharField(max_length=10)
    address = models.TextField()
    special_instructions = models.TextField(default="No special instructions")
    date = models.DateTimeField()

    def __str__(self):
        return self.flavor
    
class Order(models.Model):
    flavor = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date = models.DateTimeField()
    def __str__(self):
        return self.address