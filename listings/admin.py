from django.contrib import admin
from .models import Listing

# Dodajemy teraz tabele listings do panelu admina
admin.site.register(Listing)