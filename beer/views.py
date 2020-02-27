from django.views.generic import ListView, DetailView

from beer.models import Beer, Brewery

# Create your views here.
class BeerList(ListView):
    model = Beer

class BeerDetail(DetailView):
    model = Beer

class BreweryList(ListView):
    model = Brewery

class BreweryDetail(DetailView):
    queryset = Brewery.objects.all_with_prefetch_beers()
