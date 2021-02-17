from django.urls import path
# Ten import pozwala uzywac funkcji path()

from . import views

urlpatterns = [
    # Gdy sciezka po domenie bedzie pusta, odpal funkcje index w pliku views
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
