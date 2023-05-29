from django.db import models
from accounts.models import User
from django.utils.translation import gettext as _
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    datetime_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/blog/',blank=True,null=True)
    category = models.ForeignKey("Category",verbose_name=_("دسته بندی"),on_delete=models.CASCADE,null=True,related_name='blog')
    tags = models.ManyToManyField('Tag', verbose_name=("تگ ها"),related_name='blogs',blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(_('عنوان لاتین'))
    published_at = models.DateTimeField(_("تاریخ انتشار"),auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_('عنوان لاتین'))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    blog =models.ForeignKey('Blog',verbose_name=_('مقاله'), related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(_('متن تظر'))
    date = models.DateField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.blog.title

