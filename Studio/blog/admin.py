from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','category')
    list_filter = ('title',)
    search_fields = ('category',)
    ordering = ('created_at',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','date')
    date_hierarchy = 'date'



admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments,CommentAdmin)