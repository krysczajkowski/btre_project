from django.contrib import admin
from .models import Realtor

# Wyjasnienia wszystkiego w listings/admin.py
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_filter = ('is_mvp',)
    search_fields = ('name', 'email')
    list_per_page = 25



# Dodajemy teraz tabele Realtor do panelu admina
admin.site.register(Realtor, RealtorAdmin)
