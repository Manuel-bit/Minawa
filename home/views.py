from django.shortcuts import render
from .models import CarouselProducts

# Create your views here.

def Home(request):
    product = CarouselProducts.objects.all()
    context = {
        'product':product ,
    }
    return render(request, 'home/index.html', context)
