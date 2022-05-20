from django.core.exceptions import ValidationError
from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)

    def clean(self):
        password = self.password
        password1 = self.password1
        if password and password1 and password != password1:
            raise ValidationError('password do not match')
        return password1

    def __str__(self):
        return str(self.username)


class Product(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['images', str(instance.name), filename])

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=110)
    price = models.IntegerField()
    file = models.FileField(upload_to=nameFile)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)
