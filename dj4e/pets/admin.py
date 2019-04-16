from django.contrib import admin
from pets.models import Kind, Pet

# Register your models here.

admin.site.register(Kind)
admin.site.register(Pet)
