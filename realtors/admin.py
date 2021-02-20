from django.contrib import admin
from .models import Realtor


# Dodajemy teraz tabele Realtor do panelu admina
admin.site.register(Realtor)
