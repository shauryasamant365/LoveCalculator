from django.db import models

# Create your models here.
class Calculation(models.Model):
    username = models.CharField(default="", max_length=50)
    partner = models.CharField(default="", max_length=50)
    percentage = models.IntegerField(default="")

    def __str__(self):
        return f"{self.username.split(' ')[0].title()} and {self.partner.split(' ')[0].title()} ({self.percentage})"  


class Contact(models.Model):
    name = models.CharField(default="", max_length=50)
    email = models.EmailField(default="")
    subject = models.CharField(default="", max_length=300)
    message = models.TextField(default="")
