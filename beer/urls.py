from django.urls import path

from . import views

app_name = 'beer'
urlpatterns = [
    path('beers',
        views.BeerList.as_view(),
        name='BeerList'),
    path('beer/<int:pk>',
        views.BeerDetail.as_view(),
        name='BeerDetail'),
    path('breweries',
        views.BreweryList.as_view(),
        name='BreweryList'),
    path('brewery/<int:pk>',
        views.BreweryDetail.as_view(),
        name='BreweryDetail'),
    path('beer/<int:beer_id>/vote',
        views.CreateVote.as_view(),
        name='CreateVote'),
    path('beer/<int:beer_id>/vote/<int:pk>',
        views.UpdateVote.as_view(),
        name='UpdateVote'),
    path('beer/<int:beer_id>/image/upload',
        views.BeerImageUpload.as_view(),
        name='BeerImageUpload'),
]