from django.contrib import admin
from .models import Image
# Register your models here.

@admin.register(Image)
class Imageadmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'date') # Display the id, photo, and date fields in the admin interface.