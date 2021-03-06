from django.shortcuts import render
from django.http import HttpResponse
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices
# Create your views here.


def index(request):
    # Sortujemy po dacie, od najnowszych
    # Pobieramy tylko pierwsze 3 [:3]
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    data = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    
    return render(request, 'pages/index.html', data)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    # Get mvp realtor 
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    data = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', data)
