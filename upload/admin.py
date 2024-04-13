from django.contrib import admin
from .models import Photo
from django import forms

class PhotoAdmin(admin.ModelAdmin):
    class Meta:
        list_display = [' created_at']

admin.site.register(Photo, PhotoAdmin)

# Register your models here.
