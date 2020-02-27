from django.contrib import admin

# Register your models here.
from beer.models import Beer, Brewery, Hop, Style

admin.site.register(Beer)
admin.site.register(Brewery)
admin.site.register(Hop)
admin.site.register(Style)
