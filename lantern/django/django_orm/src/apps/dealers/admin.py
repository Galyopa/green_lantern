from django.contrib import admin

from apps.dealers.models import Dealer, City, Country


@admin.register(Dealer)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'title')
    

@admin.register(City)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Country)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
