from django.contrib import admin
from .models import Listing

# Ta klasa pozwoli nam zmienic wyglad w panelu admin, tu: http://127.0.0.1:8000/admin/listings/listing/
# To dzieki niej mamy tą tabelke
class ListingAdmin(admin.ModelAdmin):
    # Podajemy wartosci do tabelki; ta zmienna musi sie tak nazywac
    list_display = ('id', 'title', 'is_published', 'price', 'realtor')

    # Tu podajemy w co chcemy miec mozliwosc kliknac po wiecej szczegolow 
    list_display_links = ('id', 'title', 'is_published', 'price', 'realtor')

    # Tu podajemy przez co chcemy miec mozliwosc filtrowania tej tabeli, to to po prawej
    # Gdy mamy jeden parametr na koncu MUSI byc przecinek; nwm czemu, ale musi
    list_filter = ('realtor',)

    # To sprawia ze mamy search bar, w nawiasach sa wartosci po ktorych mozemy szukac
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')

    list_per_page = 25
# Dodajemy teraz tabele listings do panelu admina
admin.site.register(Listing, ListingAdmin)