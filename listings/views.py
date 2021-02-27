from django.shortcuts import render, get_object_or_404
# Importujemy model listing
from .models import Listing
# Importujemy paginatora i jeszcze jakies pierdy 
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

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
    # bierzemy pole id z modelu Listing i przyrownujemy je do listing_id
    # id=listing_id
    listing = get_object_or_404(Listing, id=listing_id)

    data = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', data)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Sprawdzamy czy sa jakies keywordy w zapytaniu get (to ten search)
    if 'keywords' in request.GET:
        # Btw. te nazwy 'city', 'keywords' bierzemy z atrybutu name w formularzu html z pliku search
        keywords = request.GET['keywords']

        if keywords:
            # Sprawdzamy czy w polu description w bazie danych sa keywordsy ktore wpisal uzytkownik
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # Miasto
    if 'city' in request.GET:
        city = request.GET['city']

        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Stan
    if 'state' in request.GET:
        state = request.GET['state']

        if state:
            queryset_list = queryset_list.filter(state__iexact=state)


    # Sypialnie
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        if bedrooms:
            # Funkcja lte wybierze nam wszystkie lazienki DO tej cyfry
            # Czyli jesli wybrales 4, to ona pokaze mieszkania z 1,2,3 i 4
            # Jest bedroom__lte bo w bazie danych to pole nazywa sie bedroom, a w url bedrooms
            # Tu odowolujemy sie do bazy danych, wiec 
            queryset_list = queryset_list.filter(bedroom__lte=bedrooms)


    # Cena
    if 'price' in request.GET:
        price = request.GET['price']

        if price:
            # Funkcja lte wybierze nam wszystkie lazienki DO tej cyfry
            # Czyli jesli wybrales 4, to ona pokaze mieszkania z 1,2,3 i 4
            # Jest bedroom__lte bo w bazie danych to pole nazywa sie bedroom, a w url bedrooms
            # Tu odowolujemy sie do bazy danych, wiec 
            queryset_list = queryset_list.filter(price__lte=price)

    data = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', data)