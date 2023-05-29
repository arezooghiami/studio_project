from django.db import models
from home.models import *
from django.utils.translation import gettext as _
# Create your models here.
class Photos(models.Model):
    PHOTO_TYPE = [
        ('All','All'),
        ('portrait','پرتره'),
        ('adv','تبلیغاتی'),
        ('studio','studio'),
        ('outdoor','فضای باز'),
        ('تولد','تولد'),
        ('مراسم','مراسم'),
        ('کودک','کودک'),

    ]
    pub_date = models.DateField(auto_now=False,auto_now_add=True)
    photo = models.ImageField(upload_to='photo/')
    type_photo = models.CharField(max_length=10, choices=PHOTO_TYPE, default='All')


    def __str__(self):
        return self.type_photo

# class Photo_detail(models.Model):
#     category = models.ForeignKey(Category)
#     name = models.CharField(max_length=100)
#     limited = models.TextField()
#     create = models.DateField(auto_now=False,auto_now_add=True)
#     image = models.ImageField(upload_to='photos')
#     like = models.ManyToManyField(User, blank=True, related_name='photo_like')
#     total_like = models.PositiveIntegerField(default=0)
#     unlike = models.ManyToManyField(User, blank=True, related_name='photo_unlike')
#     total_unlike = models.PositiveIntegerField(default=0)
#     favorite = models.ManyToManyField(User, blank=True, related_name='fa_user')
#     total_favorite = models.IntegerField(default=0)
#     view = models.ManyToManyField(User, blank=True, null=True, related_name='photo_view')
#     num_view = models.IntegerField(default=0)
#
#
#     def total_like(self):
#         return self.like.count()
#
#     def total_unlike(self):
#         return self.unlike.count()

#