from django.shortcuts import render
# Importujemy model listing
from .models import Listing
# Importujemy paginatora i jeszcze jakies pierdy 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    # Pobieramy wszystkie zmienne/parametry w listing
    # Sortujemy je po dacie, na poczatku jest minus bo chcemy od najwczesniejszych
    # Jesli chcesz bez sortowania to uzyj Listing.objects.all()
    # Dzieki funkcji filter, wyswietlamy tylko te listingi ktore spelniaja warunek w nawiasach
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    # Dane dla pliku html musimy podac jako dictionary
    data = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', data)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')