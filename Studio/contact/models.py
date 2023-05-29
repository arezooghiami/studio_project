from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    massege = models.TextField(null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
