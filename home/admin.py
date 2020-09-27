from django.contrib import admin
from .models import CarouselProducts, Quotation

# Register your models here.

class CarouselProductsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(CarouselProducts)

class QuotationAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Quotation)