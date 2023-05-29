from django.db import models
from django.urls import reverse
from accounts.models import User
from taggit.managers import TaggableManager
from django.forms import ModelForm
from django.db.models import Avg
from django_jalali.db import models as jmodels
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام دسته بندی')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True,unique=True,null=True,blank=True)
    image = models.ImageField(upload_to='category',null=True,blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=100)
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.PositiveIntegerField()
    information = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/product')

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price) / 100
            return int(self.unit_price - total)
        return self.total_price

class Variatns(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    product_variant = models.ForeignKey(Product,on_delete=models.CASCADE)
    size_variant = models.ForeignKey(Size,on_delete=models.CASCADE,null=True,blank=True)
    unit_price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
