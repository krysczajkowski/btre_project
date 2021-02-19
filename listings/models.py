from django.db import models
from datetime import datetime
# Z aplikacji (app) realtors z pliku models zaimportuj klase Realtor
from realtors.models import Realtor

# To sa kolumny w bazie danych generalnie
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    # blank=True czyli te pole NIE jest wymagane, jesli zostanie puste nie wyjebie errora
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedroom = models.IntegerField()
    # max_digits czyli ilosc cyfr, np 22 to 2, 1000 to 4
    # decimal_places to ilosc miejsc po przecinku
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    #default=0 czyli wartosc domyslna tego pola to 0
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    #upload_to czyli mamy podac sciezke do ktorej ma isc zdjecie
    # 'photos/%Y%m%d/' czyli ma isc do folderu photos/aktualna data
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    # Ta funkcja sprawia ze w admin area kolumna title bedzie ta glowna
    def __str__(self):
        return self.title

