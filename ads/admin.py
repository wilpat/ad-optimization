from django.contrib import admin

# Register your models here.
from .models import Ad, Interaction

admin.site.register(Ad)
admin.site.register(Interaction)