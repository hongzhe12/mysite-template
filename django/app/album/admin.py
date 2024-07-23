from django.contrib import admin

# Register your models here.
from .models import Album, Photo

# Register your models here.

admin.site.register(Album)
admin.site.register(Photo)
