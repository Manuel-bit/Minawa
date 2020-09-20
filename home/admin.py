from django.contrib import admin
from .models import CarouselProducts

# Register your models here.

class CarouselProductsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(CarouselProducts)